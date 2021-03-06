# Generated by Django 3.2.6 on 2021-08-16 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_with_job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('profile_photo', models.ImageField(upload_to='students_with_job/profiles')),
                ('company_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='student_application_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eduction', models.CharField(max_length=50)),
                ('finished_in', models.DateField()),
                ('alternative_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('starting_salary', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(upload_to='posts/main_images/')),
                ('education_needed', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('part_or_full_time', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('office_or_home', models.CharField(choices=[('Work from home', 'Work from home'), ('Office', 'Office')], max_length=100)),
                ('vacancies', models.PositiveSmallIntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('descriptions', models.TextField(verbose_name='')),
                ('breaking_rules', models.BooleanField(default=False)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='form_of_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('eduction', models.CharField(max_length=50)),
                ('finished_in', models.DateField()),
                ('alternative_number', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_post', to='job.job_post')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
