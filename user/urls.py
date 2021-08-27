from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.login, name="login"),
    path('sign-up/',views.signup, name="signup"),
    path('become-teacher/', views.create_teacher , name="become_teacher")
]
