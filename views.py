#from django.shortcuts import render

from djano.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')
# Create your views here.
