from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('',views.listar, name='listar'),
    path('alumnosAdd',views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>',views.alumnos_del, name='alumnos_del'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
    path('alumnos_finEdit/<str:pk>',views.alumnos_findEdit, name='alumnos_findEdit'),        
]
