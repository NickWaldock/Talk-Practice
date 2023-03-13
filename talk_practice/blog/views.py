from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm


# View list of all posts
def post_list(request):
    list = BlogPost.objects.all()
    context = {
        "list": list
    }
    return render(request, "post-list.html", context)

# View a single post in full page
def get_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    context = {
        "post": post
    }
    return render(request, "single-post.html", context)

# Create a new post
def create_post(request):
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }
    return render(request, "create-post.html", context)

# Update a post
def update_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    form = BlogPostForm(instance=post)

    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }
    return render(request, "edit-post.html", context)

# Delete a post
def delete_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    post.delete()
    return redirect('/')