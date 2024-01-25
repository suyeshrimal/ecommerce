# Generated by Django 4.2.8 on 2024-01-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
