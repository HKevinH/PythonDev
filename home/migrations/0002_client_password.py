# Generated by Django 5.0.3 on 2024-03-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='123456', max_length=50, verbose_name='Password'),
        ),
    ]
