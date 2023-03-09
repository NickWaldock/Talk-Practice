from django.shortcuts import render
from .models import BlogPost


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