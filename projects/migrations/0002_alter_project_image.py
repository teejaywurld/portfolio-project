# Generated by Django 4.0.4 on 2022-04-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.TextField(default='https://thumbs.dreamstime.com/b/project-management-concept-27391266.jpg'),
        ),
    ]
