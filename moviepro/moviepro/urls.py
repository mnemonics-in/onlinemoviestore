"""
URL configuration for moviepro project.

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
from django.urls import path
from movieapp import views

from django.conf import settings
from django.conf.urls.static import static

app_name='movieapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name="index"),#Function based views path
    path('',views.MovieList.as_view(),name="index"),

    # path('add',views.addmovie,name="addmovie"),
    path('add/',views.Movieadd.as_view(),name="add_movie"),

    # path('viewmovie/<int:p>',views.viewmovie,name="viewmovie"),
    path('detail/<int:pk>',views.MovieDetail.as_view(),name="detail"),

    # path('moviedelete/<int:p>',views.moviedelete,name="moviedelete"),
    path('delete/<int:pk>',views.Moviedelete.as_view(), name='delete'),

    # path('mvoieedit/<int:p>',views.movieedit,name="movieedit"),
    path('update/<int:pk>',views.Movieupdate.as_view(),name="update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)