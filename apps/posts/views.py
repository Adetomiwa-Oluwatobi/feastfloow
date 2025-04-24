import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Class-based view for the newsfeed (list of posts)
class PostListView(ListView):
    model = Post
    template_name = 'posts/newsfeed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # Show latest posts first

    def get_queryset(self):
        # Fetch the posts for the newsfeed
        return Post.objects.all()

# Class-based view for creating a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:newsfeed')  # Redirect to newsfeed after creation

    def form_valid(self, form):
        # Set the user as the post author
        form.instance.author = self.request.user
        return super().form_valid(form)

# View to handle liking a post
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Unliking the post
    return JsonResponse({'like_count': post.post_likes.count()})

# View to handle commenting on a post

def post_comment(request, post_id):
    if request.method == "POST":
        # Ensure content is in the body of the request
        try:
            data = json.loads(request.body)
            content = data.get('content', '').strip()
            
            if not content:
                return JsonResponse({'error': 'Comment content cannot be empty.'}, status=400)
            
            post = Post.objects.get(id=post_id)
            comment = Comment.objects.create(author=request.user, post=post, content=content)
            
            # Return the new comment data in response
            return JsonResponse({
                'author': comment.author.username,
                'content': comment.content,
                'created_at': comment.created_at,
            })
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method.'}, status=405)



@login_required
def post_detail(request, post_id):
    # Retrieve the post object by ID or return a 404 error if not found
    post = get_object_or_404(Post, id=post_id)
    
    # Handle likes via an AJAX request (optional for interactive like button)
    if request.method == "POST" and request.is_ajax():
        if request.user in post.likes.all():
            post.likes.remove(request.user)  # Unlike the post
            liked = False
        else:
            post.likes.add(request.user)  # Like the post
            liked = True
        
        # Respond with JSON for dynamic like button updates
        return JsonResponse({"liked": liked, "like_count": post.likes.count()})

    # Handle new comment submission if a form is posted
    if request.method == "POST" and not request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create and save a new comment instance
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', post_id=post.id)
    else:
        form = CommentForm()  # Display an empty form

    # Render the post details with associated comments
    context = {
        'post': post,
        'comments': post.post_comments.all().order_by('-created_at'),
        'form': form,
    }
    return render(request, 'posts/post_detail.html', context)