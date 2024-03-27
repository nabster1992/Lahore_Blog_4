from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm
import logging

# Create your views here.



def blog_index(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 3 )
    page_number = request.GET.get('page', 1)
    page = int(page_number)
    try:
        posts = paginator.page(page)
    except:
        return HttpResponse('')
    



    context = {
        'posts': posts,
        'page': page
    }

    if request.htmx:
        return render(request, 'snippets/loop_index_posts.html', context)
    
    return render(request, 'Blog/index.html', context )

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-date_added")

   
    context = {
        'category': category,
        'posts': posts,
    }


    # you use a Django Queryset filter. The argument of the filter tells Django what conditions need to be true to retrieve an object. In this case, you only want posts whose categories contain the category with the name corresponding to what’s given in the argument of the view function.
    return render(request, 'Blog/blog_category.html', context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
     # The blog_detail() view function takes a primary key value, pk, as an argument and, on line 6, retrieves the object with the given pk. The primary key is the unique identifier of a database entry. That means you’re requesting a single post with the specific primary key that you provide.
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog_detail', post.pk)
    else:
        form = CommentForm()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, 'Blog/blog_detail.html', context)

def resturaunts(request):
    return render(request, 'Blog/latest_resturaunts.html')

def privacy_policy(request):
    return render(request, 'Blog/privacy_policy.html')


def disclaimer(request):
    return render(request, 'Blog/disclaimer.html')

def contact_us(request):
    return render(request, 'Blog/contact_us.html')

   


    


# Create your views here.
