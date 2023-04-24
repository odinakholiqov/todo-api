from django.urls import path
from .views import ListTodo, DetailTodo, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]