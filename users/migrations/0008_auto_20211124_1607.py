# Generated by Django 3.2.7 on 2021-11-24 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='face_embedding',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='schoolID',
        ),
    ]
