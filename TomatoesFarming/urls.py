"""TomatoesFarming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from django.views.static import serve

from TomatoesFarmingapp.views import home, courses, quizzes, register, login_request, quiz1, logout_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home, name="home"),
    path('courses/', courses, name="courses"),
    path('quizzes/', quizzes, name="quizzes"),
    path('quiz1/', quiz1, name="quiz1"),
    path('register/', register, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name= "logout"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
