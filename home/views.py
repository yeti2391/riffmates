# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    content = "Welcome to RiffMates Home Page! by: \nMarco & Nicky"
    return HttpResponse(content, content_type="text/plain")