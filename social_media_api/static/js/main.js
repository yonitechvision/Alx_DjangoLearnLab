// User Registration
document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let bio = document.getElementById('bio').value;

    fetch('/api/accounts/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password, bio}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            document.getElementById('registerResult').innerText = 'Registration successful!';
            localStorage.setItem('token', data.token);
        } else {
            document.getElementById('registerResult').innerText = 'Error: ' + JSON.stringify(data);
        }
    })
    .catch(error => console.log(error));
});

// User Login
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('/api/accounts/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            document.getElementById('loginResult').innerText = 'Login successful!';
            localStorage.setItem('token', data.token);
        } else {
            document.getElementById('loginResult').innerText = 'Error: ' + JSON.stringify(data);
        }
    })
    .catch(error => console.log(error));
});

// Fetch Posts
function fetchPosts() {
    fetch('/api/posts/')
    .then(response => response.json())
    .then(data => {
        let postsContainer = document.getElementById('postsContainer');
        postsContainer.innerHTML = '';
        data.forEach(post => {
            postsContainer.innerHTML += `
                <div>
                    <h3>${post.title}</h3>
                    <p>${post.content}</p>
                    <p>By: ${post.author}</p>
                </div>
            `;
        });
    });
}

// Create a Post
document.getElementById('postForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let title = document.getElementById('title').value;
    let content = document.getElementById('content').value;

    fetch('/api/posts/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('token'),
        },
        body: JSON.stringify({title, content}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('postForm').reset();
        fetchPosts();  // Reload posts after creating a new one
    })
    .catch(error => console.log(error));
});

// Like a Post
document.getElementById('likeButton').addEventListener('click', function() {
    let postId = window.location.pathname.split('/')[3];  // Assuming the URL is /posts/<id>/
    fetch(`/api/posts/${postId}/like/`, {
        method: 'POST',
        headers: {
            'Authorization': 'Token ' + localStorage.getItem('token'),
        }
    })
    .then(() => {
        alert('Post liked!');
    });
});

// Follow a User
document.getElementById('followButton').addEventListener('click', function() {
    let postAuthor = document.getElementById('postAuthor').innerText;
    fetch(`/api/accounts/follow/${postAuthor}/`, {
        method: 'POST',
        headers: {
            'Authorization': 'Token ' + localStorage.getItem('token'),
        }
    })
    .then(() => {
        alert('User followed!');
    });
});

// Fetch Notifications
function fetchNotifications() {
    fetch('/api/notifications/')
    .then(response => response.json())
    .then(data => {
        let container = document.getElementById('notificationsContainer');
        container.innerHTML = '';
        data.forEach(notification => {
            container.innerHTML += `
                <div>
                    <p>${notification.actor} ${notification.verb} ${notification.target}</p>
                    <p>${new Date(notification.timestamp).toLocaleString()}</p>
                </div>
            `;
        });
    });
}
