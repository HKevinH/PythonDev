# Generated by Django 5.0.3 on 2024-03-25 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_client_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(default='123456', max_length=500, verbose_name='Password'),
        ),
    ]
