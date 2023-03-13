from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    author = models.CharField(max_length=20)
    date_updated = models.DateField()
    blog_content = models.TextField()
    
    def __str__(self):
        return self.title
    
    