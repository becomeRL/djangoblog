# Generated by Django 3.1.3 on 2020-12-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20201204_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngTexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='KorTexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ko_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='TodayTexts',
        ),
    ]
