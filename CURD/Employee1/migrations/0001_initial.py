# Generated by Django 2.1.3 on 2018-11-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('local_address', models.CharField(max_length=100)),
                ('perma_address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('father', models.CharField(max_length=100)),
                ('mother', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]
