# Generated by Django 3.2.12 on 2022-03-09 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0004_alter_order_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
    ]