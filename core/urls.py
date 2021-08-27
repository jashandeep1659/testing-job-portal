from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('latest_jobs/', views.latest_jobs, name="latest_jobs"),
    path('job/<int:id>/<str:slug>/', views.job_view, name="job_view"),
    path('apply-job/<int:id>/<str:slug>', views.apply_job , name="apply_job"),
    path('my-applications/', views.my_applications , name="my_applications")
]
