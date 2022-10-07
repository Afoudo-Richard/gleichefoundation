# Generated by Django 4.0.5 on 2022-10-05 04:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='cause',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.cause'),
        ),
        migrations.AddField(
            model_name='upcomingevent',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]