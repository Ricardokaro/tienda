# Generated by Django 3.0.10 on 2020-10-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40, verbose_name='circle_name'),
        ),
    ]
