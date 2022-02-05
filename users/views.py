from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm    # imports alll the field of form from UserRegisterForm in forms.py

# Create your views here.
def register(request):
    if request.method == "POST":        # submitts as a POST request from users
        form = UserRegisterForm(request.POST)       #creates a new form based on the data in request.POST
        if form.is_valid():
            form.save()      
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! You can login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance = request.user)
        pro_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid and pro_form.is_valid():
            u_form.save()
            pro_form.save() 
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        pro_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'pro_form' : pro_form,
    }
    return render(request,'users/profile.html', context)