from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.ListPost.as_view()),
    path('api/<int:pk>/', views.test),
    path('', views.main, name='main'),
    path('postwrite/', views.PostWrite, name='postwrite'),
]
