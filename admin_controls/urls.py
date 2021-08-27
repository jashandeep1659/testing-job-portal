from django.urls import path
from . import views

urlpatterns = [
    path('teacher-controls/', views.teacher_controls , name='teacher_controls'),
    path('all-users/',views.all_users, name="all_users"),
]
