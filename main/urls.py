from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.home),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),
    path('create', views.create),
    path('view/<id>', views.view)
]
