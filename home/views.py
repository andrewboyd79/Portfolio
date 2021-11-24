from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def services(request):
    """ A view to return the about page """

    return render(request, 'home/services.html')


def price(request):
    """ A view to return the about page """

    return render(request, 'home/price.html')


def elements(request):
    """ A view to return the about page """

    return render(request, 'home/elements.html')
