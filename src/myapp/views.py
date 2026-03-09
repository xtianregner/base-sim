from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'myapp/index.html')


def services(request):
    return render(request, 'myapp/services.html')


def about(request):
    return render(request, 'myapp/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, f'¡Gracias {name}! Tu mensaje ha sido enviado. Te contactaremos pronto.')
        return redirect('contact')
    return render(request, 'myapp/contact.html')


def api_data(request):
    data = {
        'app': 'Puppy Fly Time',
        'status': 'success'
    }
    return JsonResponse(data)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'index'
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'myapp/login.html', {
        'next': request.GET.get('next', '')
    })


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('index')