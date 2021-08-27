from django.db import models
from django.db.models.base import Model
from user.models import User

# Create your models here.
class Student_with_job(models.Model):
    id  = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=50)
    slug  = models.SlugField(max_length=150, unique =True)
    description  = models.TextField()
    profile_photo  = models.ImageField(upload_to='students_with_job/profiles')
    company_name  = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Job_Post(models.Model):
    id  = models.AutoField(primary_key =True)
    part_or_full = (
    ('Full Time', 'Full Time'),
    ('Part Time','Part Time')
    )
    home_office  = (
    ('Work from home', 'Work from home'),
    ('Office','Office')
    )
    by  = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    starting_salary  = models.PositiveSmallIntegerField()
    image  = models.ImageField(upload_to='posts/main_images/')
    education_needed = models.CharField(max_length=100,)
    location  = models.CharField(max_length=100)
    part_or_full_time  = models.CharField(max_length=100, choices = part_or_full)
    skills  = models.CharField(max_length=100,)
    office_or_home = models.CharField(max_length=100, choices = home_office)
    vacancies  = models.PositiveSmallIntegerField()
    company_name = models.CharField(max_length=100)
    descriptions = models.TextField(verbose_name='')
    breaking_rules  = models.BooleanField(default=False)
    posted_at = models.DateTimeField( auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    # objects = Job_Post_Manger()


class student_application_data(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    eduction  = models.CharField(max_length=50)
    finished_in  = models.DateField()
    alternative_number  = models.IntegerField()
    age = models.IntegerField()
    address  = models.TextField()
    city = models.CharField(max_length=50)
    pin_code  = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.eduction


class form_of_post(models.Model):
    id  = models.AutoField(primary_key =True)
    teacher= models.ForeignKey(User, on_delete=models.CASCADE , related_name = 'teacher')
    student = models.ForeignKey(User, on_delete=models.CASCADE , related_name ="student")
    post =  models.ForeignKey(Job_Post, on_delete=models.CASCADE , related_name ="job_post")
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email  = models.CharField(max_length=50)
    phone_number  = models.IntegerField()
    age  = models.IntegerField()
    eduction  = models.CharField(max_length=50)
    finished_in  = models.DateField()
    alternative_number  = models.IntegerField()
    address  = models.TextField()
    city = models.CharField(max_length=50)
    pin_code  = models.DecimalField(max_digits=5, decimal_places=0)


    def __str__(self):
        return self.email
