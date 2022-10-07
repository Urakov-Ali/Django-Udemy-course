from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogView(request):
    Blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog.html', {'blogs':Blogs})

def blogDetailView(request, blog_id):
    Blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog':Blog_detail})

