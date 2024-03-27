"""
URL configuration for Nabeel_Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Blog.views import blog_index, blog_detail, blog_category, privacy_policy, disclaimer, contact_us, resturaunts

urlpatterns = [
    path("", blog_index, name='index'),
    path('resturaunts/', resturaunts, name='resturaunts'),
    path('disclaimer/', disclaimer, name='disclaimer'),
    path('contact_us/', contact_us, name='contact_us'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('post/<int:pk>/', blog_detail, name='blog_detail'),  # Ensure a trailing slash
    path('category/<str:category>/', blog_category, name='blog_category'),  # Add this line
    path('admin/', admin.site.urls)
]  + static(settings.STATIC_URL, document_root = settings.STATIC_URL) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
