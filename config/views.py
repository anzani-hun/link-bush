from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required


from links.models import MyLink

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    my_links = MyLink.objects.filter(user = request.user )
    return render(request, 'index.html', {'links':my_links})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user = authenticate(
                request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
        
            if user is not None:
                login(request, user)
                return redirect('index')

    login_form = AuthenticationForm()

    return render (request, 'login.html',
                    {"form" : login_form})