# Generated by Django 3.0.10 on 2020-10-09 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modifico por ultima vez el objeto.', verbose_name='modified at')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=140)),
                ('price', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('stock_limited', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modifico por ultima vez el objeto.', verbose_name='modified at')),
                ('total', models.PositiveIntegerField(default=0, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modifico por ultima vez el objeto.', verbose_name='modified at')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=140)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creo el objeto.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modifico por ultima vez el objeto.', verbose_name='modified at')),
                ('unit_value', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Purchase')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(through='stores.PurchaseDetail', to='stores.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store'),
        ),
    ]
