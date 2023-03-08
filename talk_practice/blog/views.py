from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def post_list(request):
    list = BlogPost.objects.all()
    context = {
        "list": list
    }
    return render(request, "post-list.html", context)