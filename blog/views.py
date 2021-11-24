from django.shortcuts import render

# Create your views here.


def blog(request):
    """ A view to return the index page """

    return render(request, 'blog/blog.html')


def post(request):
    """ A view to return the index page """

    return render(request, 'blog/post.html')
    