# Generated by Django 4.0.4 on 2022-04-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.TextField(default='https://files.realpython.com/media/13-Python-Projects-for-Intermediate-Developers_Watermarked.bb98d44bdb10.jpg'),
        ),
    ]