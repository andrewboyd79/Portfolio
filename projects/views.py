from django.shortcuts import render

# Create your views here.


def projects(request):
    """ A view to return the index page """

    return render(request, 'projects/projects.html')
