# Generated by Django 3.2.7 on 2021-12-24 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20211223_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newbook',
            name='synopsis',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
