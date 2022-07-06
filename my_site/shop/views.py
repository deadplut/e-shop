from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'shop/home.html', context)

def about(request):
    return render(request, 'shop/about.html', {'title': 'О клубе Python Bytes'})