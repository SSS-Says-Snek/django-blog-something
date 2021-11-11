from django.db import models


# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_description = models.CharField(max_length=400, blank=True, default='')
    post_content = models.TextField()
    date_posted = models.DateTimeField("date posted")

    def __str__(self):
        return f"Post: \"{self.post_title[:50]}\""
