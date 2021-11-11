from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.


def home(request):
    return render(request, "main/index.html", context={
        "posts": Post.objects.all
    })
