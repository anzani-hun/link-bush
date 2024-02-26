from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            user = authenticate(
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
        
            if user is not None:
                login(request, user)
                return redirect('index')

    login_form = AuthenticationForm()

    return render(request, 'login.html',
                    {"form" : login_form})