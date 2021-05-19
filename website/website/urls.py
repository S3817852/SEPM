"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views
from core.views import frontpage, signup



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('product/', include('owner.urls')),
    # path('create/', include('owner.urls')),
    # path('details/', include('owner.urls')),
    # path('delete/', include('owner.urls')),
    path('home/', include('home.urls')),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('announcement/', include('announcement.urls')),
    path('notification/', include('notification.urls')),
    path('house/', include('house.urls')),
    path('tenant/', include('tenant.urls')),
    path('ew/', include('EW.urls')),
    path('billandreceipts/', include('BillAndReceipts.urls')),
    path('roomservices/', include('roomservices.urls')),
    path('account/', include('userprofile.urls')),
    # path('', include('home.urls')),
    # path('notifications/', include('notification.urls')),
    # path('job/', include('job.urls')),
    # path('dashboard/', include('userprofile.urls')),
    # path('', frontpage, name='frontpage'),
    # path('signup/', signup, name='signup'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login')
]
