# Generated by Django 4.0.4 on 2023-02-12 19:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_remove_book_book_status_book_is_issued_visitors_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visitors',
            new_name='Visitor',
        ),
    ]
