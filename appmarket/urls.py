"""
URL configuration for appmarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.login_view, name='home'),
    path('customer/', views.customer_dashboard, name='customer-home'),
    path('dashboard/', views.customer_dashboard, name='customer-dashboard'),
    path('provider/', views.provider_dashboard, name='provider-dashboard'),
    path('projects/create/', views.project_create, name='project-create'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/select-role/', views.select_role, name='select-role'),
    path('accounts/choose-role/', views.choose_role, name='choose-role'),
    path('accounts/login/', views.account_login, name='account-login'),
    path('accounts/logout/', views.account_logout, name='account-logout'),
]
