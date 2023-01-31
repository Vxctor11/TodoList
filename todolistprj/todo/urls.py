from django.urls import path
from .views import Tasklist, TaskDetail, TraskCreate, TaskUpdate, TaskDelete, UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', Tasklist.as_view(), name='task'),
    path('task-create/',TraskCreate.as_view(), name='task-create'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete"),
]