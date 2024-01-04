# Generated by Django 4.2.8 on 2024-01-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='p', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='l', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]