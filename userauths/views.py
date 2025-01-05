from django.shortcuts import redirect, render
from appSettings import settings
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.
# user = settings.AUTH_USER_MODEL

def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    
    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = UserRegisterForm()
    # context = {
    #     'form': form,
    # }
    return render(request, 'new_snip.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')