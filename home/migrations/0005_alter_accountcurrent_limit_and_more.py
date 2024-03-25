# Generated by Django 5.0.3 on 2024-03-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_client_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountcurrent',
            name='limit',
            field=models.DecimalField(decimal_places=2, default='0.5', max_digits=10, verbose_name='Limit'),
        ),
        migrations.AlterField(
            model_name='accountsaving',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, default='0.5', max_digits=5, verbose_name='Interest Rate'),
        ),
    ]
