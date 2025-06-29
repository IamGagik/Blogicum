from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lt=timezone.now())[0:5]
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, id: int):
    """Страница отдельного поста."""
    template = 'blog/detail.html'
    current_post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__date__lt=timezone.now()
        ),
        id=id
    )
    context = {
        'post': current_post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категорий."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__date__lt=timezone.now())

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template, context)
