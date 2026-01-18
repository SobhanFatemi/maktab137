from django.http import(
    HttpRequest,
    HttpResponse
)

from django.shortcuts import render

# Create your views here.
def home_page(request):
    print(request.headers)
    return HttpResponse("Hello, World")

