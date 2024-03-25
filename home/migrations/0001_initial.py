# Generated by Django 5.0.3 on 2024-03-25 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_account', models.CharField(max_length=10, unique=True, verbose_name='Account Number')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Balance')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=100, verbose_name='Street Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=2, verbose_name='State')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Zip Code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='AccountCurrent',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.account')),
                ('limit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Limit')),
            ],
            bases=('home.account',),
        ),
        migrations.CreateModel(
            name='AccountSaving',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.account')),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Interest Rate')),
            ],
            bases=('home.account',),
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.client', verbose_name='Client'),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(verbose_name='Month')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.account', verbose_name='Account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
                ('type', models.CharField(max_length=1, verbose_name='Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.account', verbose_name='Account')),
            ],
        ),
    ]