from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome aboard, {username}! Your account has been created. Log In to get started.')
            return redirect('landing-login')
    else:
        form = UserRegisterForm()

    return render(request, 'landing/register.html', {'form': form})