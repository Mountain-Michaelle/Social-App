from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.

def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard',})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully!')
                else:
                    return HttpResponse('Account Deactivated')
            else:
                return HttpResponse('Invalid password or username')
        
    else:
        form = LoginForm()
    
    context = {'form':form} 
    return render(request, 'accounts/login.html', context)