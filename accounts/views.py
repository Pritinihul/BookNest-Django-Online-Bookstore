from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Generate username internally
            user.username = user.email

            user.set_password(form.cleaned_data['password'])

            user.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{
                 'error': 'Invalid email or password.'
            })
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')