# Generated by Django 4.2.4 on 2023-09-12 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_product_name_alter_product_unityprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='unity_price',
            new_name='price',
        ),
    ]
