# Generated by Django 3.2.13 on 2022-06-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('mobile_no', models.IntegerField()),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('accept', models.BooleanField(default=False)),
            ],
        ),
    ]
