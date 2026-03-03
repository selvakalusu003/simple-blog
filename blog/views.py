from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def home(request):
    post_list = Post.objects.all().order_by('-created_date')
    paginator = Paginator(post_list, 5)  # 5 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post': post})