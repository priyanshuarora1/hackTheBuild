# Generated by Django 3.0.8 on 2020-10-03 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import members.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chat_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatid', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('sender', models.CharField(max_length=100)),
                ('reciever', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='latestmessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatid', models.CharField(max_length=200)),
                ('myid', models.CharField(max_length=100)),
                ('fid', models.CharField(max_length=200)),
                ('flag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('stuid', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('photo', models.ImageField(default='student/default.jpg', max_length=255, upload_to=members.models.path_rename_student)),
                ('coverphoto', models.ImageField(default='student/coverphoto.jpg', upload_to=members.models.path_rename_student)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teachermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('empid', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('photo', models.ImageField(default='teacher/default.jpg', max_length=255, upload_to=members.models.path_rename)),
                ('coverphoto', models.ImageField(default='teacher/coverphoto.jpg', upload_to=members.models.path_rename)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='upload_reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.CharField(max_length=100)),
                ('empphoto', models.CharField(max_length=100)),
                ('emplink', models.CharField(max_length=100)),
                ('empname', models.CharField(max_length=100, null=True)),
                ('review', models.TextField()),
                ('time', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='upload_posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('photolink', models.CharField(default='student/default.jpg', max_length=100)),
                ('profilelink', models.CharField(max_length=100)),
                ('designation', models.BooleanField()),
                ('name', models.CharField(max_length=100, null=True)),
                ('desc', models.TextField()),
                ('time', models.CharField(max_length=200, null=True)),
                ('link', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to='post/images')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='upload_achievements_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=200)),
                ('link', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to='achievements/student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='upload_achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=200)),
                ('link', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to='achievements/student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.studentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='teacherdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='Hello! I am a Teacher.', max_length=500)),
                ('dob', models.DateField(null=True)),
                ('websiteurl', models.CharField(max_length=200, null=True)),
                ('fblink', models.CharField(max_length=200, null=True)),
                ('githublink', models.CharField(max_length=200, null=True)),
                ('linkedinlink', models.CharField(max_length=200, null=True)),
                ('instalink', models.CharField(max_length=200, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='studentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='Hello! I am a student.', max_length=500)),
                ('dob', models.DateField(null=True)),
                ('websiteurl', models.CharField(max_length=200, null=True)),
                ('fblink', models.CharField(max_length=200, null=True)),
                ('githublink', models.CharField(max_length=200, null=True)),
                ('linkedinlink', models.CharField(max_length=200, null=True)),
                ('instalink', models.CharField(max_length=200, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.studentmodel')),
            ],
        ),
    ]
