from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,  CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CommentForm
from .models import Post, Comment
from taggit.models import Tag
from django.db.models import 
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'blog/home.html')

# Authentication views
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile view
def profile(request):
    return render(request, 'blog/profile.html')

# Post views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')  # Redirect after update

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Comment views
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        # Associate the comment with the post
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/edit_comment.html'

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/confirm_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  # Specify the fields for the new post
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')  # Redirect after creation

from django.shortcuts import render
from .models import Post
from taggit.models import Tag  # If you are using django-taggit

def post_list_view(request):
    query = request.GET.get('q')
    posts = Post.objects.all()

    if query:
        # Filter posts by title, content, or tags
        posts = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            content__icontains=query
        ) | Post.objects.filter(
            tags__name__icontains=query  # Assuming you are using tags with django-taggit
        )

    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'post_list.html', context)

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tagsnameicontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=tag_slug)

