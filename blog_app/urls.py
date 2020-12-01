from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('memo/', views.memo, name='memo'),
    path('memo/<int:pk>/',views.detail_memo, name='detail_memo'),
    path('new_memo/', views.new_memo, name='new_memo'),
    path('memo/<int:pk>/remove_memo/', views.remove_memo, name='remove_memo'),
]