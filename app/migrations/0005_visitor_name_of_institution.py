# Generated by Django 4.0.4 on 2023-02-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_book_id_book_issue_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='name_of_institution',
            field=models.CharField(default='NIT Durgapur', max_length=100),
            preserve_default=False,
        ),
    ]
