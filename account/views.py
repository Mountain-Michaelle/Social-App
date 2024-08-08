from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages



# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard',})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
    
            new_user.set_password(
                user_form.cleaned_data['password']
            )
        
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'user_form': user_form})

def profile(request, profile_id):
    user = User.objects.get(profile=profile_id)
    profile = Profile.objects.get(user=profile_id)
    #profile = Profile.objects.get(user=profile_id)
    
    users = Profile.objects.filter(user=user)
    profiles = User.objects.filter(profile=profile)
    
    
    
    context = {'users': users, 'profiles': profiles}
    return render(request, 'account/profile.html', context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            # return redirect('account:profile', profile_id=request.user.id)
        else:
            messages.error(request, 'Error updating your profile')
            
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'account/edit.html', context)




# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully!')
#                 else:
#                     return HttpResponse('Account Deactivated')
#             else:
#                 return HttpResponse('Invalid password or username')
        
#     else:
#         form = LoginForm()
    
#     context = {'form':form} 
#     return render(request, 'accounts/login.html', context)