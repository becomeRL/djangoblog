# Generated by Django 3.1.3 on 2020-12-10 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20201210_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memo',
            name='image',
        ),
    ]