from django.shortcuts import redirect, render
from appSettings import settings
from userauths.forms import UserRegisterForm

# Create your views here.
user = settings.AUTH_USER_MODEL

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'userauths/register.html', context)