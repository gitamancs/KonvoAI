from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('healthcare/', views.healthcare, name='healthcare'),
    path('healthcare/chatbot/', views.chatbot, name='chatbot'),
]