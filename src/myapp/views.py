from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def home(request):
    return render(request, 'myapp/home.html')

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return HttpResponse("<h1>About</h1><p>This is a Django application template.</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1><p>Contact us at: example@email.com</p>")

def api_data(request):
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return JsonResponse(data)