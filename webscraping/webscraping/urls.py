"""webscraping URL Configuration

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
from django import views
from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name="Login"),
    path('Register/',views.Register,name="Register"),
    path('admin_dashboard/', views.admin_dashboard , name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard , name='user_dashboard'),
    path('user_logout/', views.user_logout , name='user_logout'),
    path('changepassword_user/', views.changepassword_user , name='changepassword_user'),
    path('account_user/', views.account_user , name='account_user'),
    path('imagechange/', views.imagechange , name='imagechange'),
    path('news/', views.news, name = "news"),
    path('news_scrape/', views.news_scrape, name = "news_scrape"),
    path('article/', views.article, name = "article"),
    path('weather/', views.weather, name = "weather"),
    path('user_search/', views.user_search , name='user_search'),
    path('scrap/', views.scrap , name='scrap'),
    path('users/', views.users , name='users'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

