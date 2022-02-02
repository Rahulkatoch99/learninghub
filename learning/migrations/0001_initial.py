# Generated by Django 3.2.9 on 2022-01-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=25)),
                ('ConfirmPassword', models.CharField(max_length=25)),
            ],
        ),
    ]
