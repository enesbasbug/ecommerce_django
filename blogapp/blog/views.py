from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Blog, Category

# Create your views here.
def index(request):

    # In case we want to show homepage to ones who are not signed-in, like if we do not want to show homepage to the guests.
    # it direct them to login page to sign up.
    # if not request.user.is_authenticated: 
    #     return redirect("login")



    context = {
        # "blogs" : data['blogs']
        # "blogs" : Blog.objects.all()
        "blogs" : Blog.objects.filter(is_home=True),
        "categories" : Category.objects.all(),
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        # "blogs" : Blog.objects.all()
        "blogs" : Blog.objects.filter(is_active=True),
        "categories" : Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    
    blog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog-details.html", {
        "blog": blog
        })


def blogs_by_category(request, slug):
    context = {

        "blogs" : Category.objects.get(slug = slug).blog_set.filter(is_active = True),

        # "blogs" : Blog.objects.all()
        # "blogs" : Blog.objects.filter(is_active=True, category__slug=slug), # acces the slug information from the related category in Blog object __ helps us to do that.
        "categories" : Category.objects.all(),                              
        "selected_category" : slug,
    }
    return render(request, "blog/blogs.html", context)
