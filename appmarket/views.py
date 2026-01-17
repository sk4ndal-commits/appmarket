from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm
from .models import Profile


def login_view(request):
    # For demo: reuse Django's default auth views in production
    return render(request, 'login.html')


@login_required
def customer_dashboard(request):
    # Demo context: projects list empty
    projects = []
    return render(request, 'customer/dashboard.html', {'projects': projects, 'project_create_url': '/projects/create/'})


@login_required
def project_create(request):
    if request.method == 'POST':
        # Stub: pretend we saved
        return redirect('customer-home')
    return render(request, 'project/create.html', {'cancel_url': '/'})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login and redirect to role selection
            login(request, user)
            return redirect('choose-role')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def select_role(request):
    # backward-compatible alias to choose_role
    return choose_role(request)


@login_required
def choose_role(request):
    profile = request.user.profile
    # only allow selection if role not already set
    if profile.role:
        # already selected, redirect to appropriate area
        if profile.role == 'Customer':
            return redirect('customer-home')
        else:
            return redirect('provider-dashboard')

    if request.method == 'POST':
        role = request.POST.get('role')
        if role in dict(Profile.ROLE_CHOICES):
            profile.role = role
            profile.save()
            # redirect based on role
            if role == 'Customer':
                return redirect('customer-home')
            else:
                return redirect('provider-dashboard')
        else:
            return render(request, 'accounts/choose_role.html', {'error': 'Invalid role selection.'})
    return render(request, 'accounts/choose_role.html')


def account_login(request):
    # custom login handler at /accounts/login/
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # redirect based on role
            try:
                role = user.profile.role
            except Exception:
                role = None
            if not role:
                return redirect('choose-role')
            if role == 'Customer':
                return redirect('customer-home')
            else:
                return redirect('provider-dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please check your email and password.')
    return render(request, 'accounts/login.html')


@login_required
def account_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('account-login')


@login_required
def provider_dashboard(request):
    # minimal provider dashboard
    return render(request, 'provider/dashboard.html')
