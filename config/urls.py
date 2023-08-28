"""
URL configuration for config project.

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
#
from django.contrib import admin
from django.urls import path, include
from albums import views

# Define the URL patterns for your project
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),

# Map the root URL to the album_list view, Map the URL for creating a new album - looking at an album, edit, delete
    path("", views.album_list, name="album_list"),
    path("albums/new", views.create_album, name="create_album"),
    path("albums/<int:pk>", views.album_detail, name="album_detail"),
    path("albums/<int:pk>/edit", views.edit_album, name="edit_album"),
    path("albums/<int:pk>/delete", views.delete_album, name="delete_album"),
    path('accounts/', include('registration.backends.simple.urls')),
]
