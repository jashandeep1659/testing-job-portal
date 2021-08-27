from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
	use_in_migrations =True
	def _create_user(self, email, password, **extra_fields):
		"""Create and save a User with the given email and password."""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self,email,password=None , **extra_fields):
		"""Create and save a regular User with the given email and password."""
		extra_fields.setdefault('is_active', False)
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('is_superuser', False)
		extra_fields.setdefault('user_role', 'Student')
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email,password,**extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('user_role', 'Admin')
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


# geeksforgeeks.org/how-to-use-django-field-choices/
class User(AbstractUser):
	user_role_choices = (
	('Student','Student'),
	('Teacher','Teacher'),
	('Admin','Admin'),
	)
	username = None
	email  = models.EmailField(unique=True)
	first_name  = models.CharField(max_length=50)
	last_name  = models.CharField(max_length=50)
	photo  = models.ImageField(upload_to="user/teacher/", null=True,blank=True)
	qualification  = models.CharField(max_length=50, null=True, blank =True)
	phone_number  = models.PositiveIntegerField()
	notify_me  = models.BooleanField(default=True)
	user_role = models.CharField(max_length=50, choices = user_role_choices, default = 'Student')
	last_login = models.DateTimeField(auto_now = True)
	created_at  = models.DateTimeField(auto_now_add= True)
	rejected_once = models.BooleanField(default=False)
	request_as_teacher = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name','phone_number','notify_me',]

	object = UserManager()
