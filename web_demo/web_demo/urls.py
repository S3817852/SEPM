"""web_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


from account.views import (login_page, main_page, sign_up, tenant_manage,
                           userprofile)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from property.views import house_page
from services.views import announcement, ew
from bills.views import calculate_bill_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='base_page'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('userprofile/', userprofile, name='user_profile'),
    path('signup/', sign_up, name='signup'),
    path('tenant/', include('account.urls')),
    path('house/', include('property.urls')),
    path('services/', include('services.urls')),
    path('calculate-bill/', calculate_bill_view)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
