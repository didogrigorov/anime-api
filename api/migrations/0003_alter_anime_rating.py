# Generated by Django 4.2.4 on 2023-08-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_anime_episodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='rating',
            field=models.CharField(max_length=30),
        ),
    ]