from django import forms
from django.conf import settings

user = settings.AUTH_USER_MODEL

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username', 'email', 'date_of_birth']

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    # Example of additional validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field cannot be empty')
        if len(title) < 3:
            raise forms.ValidationError('Title should be at least 3 characters long')
        return title

