# Generated by Django 4.0.5 on 2022-06-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_context_newsblog_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblog',
            name='allow_public_comments',
            field=models.BooleanField(default=False),
        ),
    ]
