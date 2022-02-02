"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from learning import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='/'),
    path('login/',views.userlogin,name='login'),
    path('about/',views.abou,name='about'),
    path('contact/',views.cont,name='contact'),
    path('signup/',views.showsignin,name='signup'),
    # path('firststep/',views.python_first,name='firststep'),
    path('profile/',views.user_profile,name='profile'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('logout/',views.user_logout,name='logout'),
]
