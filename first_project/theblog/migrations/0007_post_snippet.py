# Generated by Django 4.1.7 on 2023-07-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to read full article', max_length=255),
        ),
    ]
