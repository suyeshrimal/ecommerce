# Generated by Django 4.2.8 on 2024-01-02 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')], max_length=1),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'PENDING'), ('CF', 'CONFIRM'), ('C', 'CANCEL'), ('CP', 'COMPLETED')], default='P', max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'PENDING'), ('CF', 'CONFIRM'), ('C', 'CANCEL'), ('CP', 'COMPLETED')], default='P', max_length=50)),
                ('payment_status', models.BooleanField(default=False)),
                ('shipping_address', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.customer')),
            ],
        ),
    ]