from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
        return redirect('customer-dashboard')
    return render(request, 'project/create.html', {'cancel_url': '/'})
