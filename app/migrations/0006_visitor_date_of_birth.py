# Generated by Django 4.0.4 on 2023-02-15 13:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_visitor_name_of_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
