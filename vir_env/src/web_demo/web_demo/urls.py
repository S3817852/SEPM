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


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from products.views import product_view
from user.views import sign_up, userprofile, main_page, login_page, tenant_manage
from services.views import ew, announcement
from dong_demo.views import dong_lun

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', product_view, name='product'),
    path('mainpage/', main_page, name='base_page'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('userprofile/', userprofile, name='user_profile'),
    path('signup/', sign_up, name='signup'),
    path('tenant/', include('user.urls')),
    # path('ew/', ew, name='ew'),
    path('services/', include('services.urls')),
    path('dong_lun/', dong_lun, name='VN vo dich')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
