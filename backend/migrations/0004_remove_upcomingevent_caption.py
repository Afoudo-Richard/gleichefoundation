# Generated by Django 4.0.5 on 2022-10-14 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_cause_image_alter_executive_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingevent',
            name='caption',
        ),
    ]