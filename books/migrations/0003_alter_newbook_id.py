# Generated by Django 3.2.7 on 2021-09-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_newbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbook',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]