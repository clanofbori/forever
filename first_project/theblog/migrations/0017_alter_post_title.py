# Generated by Django 4.1.7 on 2023-09-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_alter_post_title_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]