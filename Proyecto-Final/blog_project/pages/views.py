from django.shortcuts import render, get_object_or_404
from .models import Blog

def about(request):
    return render(request, 'pages/about.html')

def pages(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/pages.html', {'blogs': blogs})

def page_detail(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)
    return render(request, 'pages/page_detail.html', {'blog': blog})
