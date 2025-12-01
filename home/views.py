from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def credits(request):
    content = "By Nicky\n& Marco"
    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = '<div> <h1>About Page</h1> <p> This is the about page of RiffMates. </p></div>'
    return HttpResponse(content, content_type="text/html")

def version(request):
    data = {
        "app": "RiffMates",
        "version": "1.0.0",
        "author": "Nicky & Marco"
    }
    return JsonResponse(data)