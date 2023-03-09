from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm


# Create your views here.
def post_list(request):
    list = BlogPost.objects.all()
    context = {
        "list": list
    }
    return render(request, "post-list.html", context)


def get_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    context = {
        "post": post
    }
    return render(request, "single-post.html", context)


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
