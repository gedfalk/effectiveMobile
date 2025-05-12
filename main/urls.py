from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('switch-user/', views.user_selection, name='user_selection'),
    path('swith-user/<int:user>/', views.switch_user, name='switch_user'),
]