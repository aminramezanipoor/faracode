# Generated by Django 5.0.7 on 2024-07-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=160)),
                ('image', models.ImageField(upload_to='project')),
            ],
        ),
    ]
