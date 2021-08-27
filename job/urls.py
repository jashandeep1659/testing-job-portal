from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name="create_post"),
    path('my-posts/', views.posts_by_teacher , name="posts_by_teacher"),
    path('students-applied/<int:id>/<slug:slug>/',views.students_apply , name="students_apply"),
    path('application-form/<int:id>/job/<int:post_id>',views.generate_pdf_through_template , name="application_form")
]
