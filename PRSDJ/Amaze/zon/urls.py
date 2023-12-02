from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("file", views.file, name='file'),
    path("prod", views.product, name='product'),
    path("sign", views.signup, name='sign')
]
