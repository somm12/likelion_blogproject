"""blogproject URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
import blog.views #import 잊지말기
import portfolio.views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',blog.views.first,name="first"),
    path('blog/',blog.views.home, name="home"),
    path('blog/<int:blog_id>',blog.views.detail, name="detail"),
    path('about_me/',blog.views.about_me, name="about_me"),
    path('about_me/email',blog.views.email, name="email"),
    path('about_me/github',blog.views.github, name="github"),
    path('about_me/instagram',blog.views.instagram, name="instagram"),

    path('blog/new',blog.views.new, name="new"),
    path('blog/create',blog.views.create, name="create"),
    path('blog/edit/<str:id>',blog.views.edit,name="edit"),
    path('blog/update/<str:id>',blog.views.update,name="update"),
    path('blog/delete/<str:id>',blog.views.delete, name="delete"),

    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
    
]
# 블로그 글 이미지 URL 설정
urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#html 이미지 업로드
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)