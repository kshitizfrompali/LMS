# Generated by Django 4.2.9 on 2024-02-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_rename_returned_dated_returnedbookdetail_returned_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnedbookdetail',
            name='fine',
            field=models.FloatField(default=0),
        ),
    ]
