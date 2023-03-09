from django.forms import ModelForm
from .models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "subtitle",
            "author",
            "date_updated",
            "blog_content",
        ]
