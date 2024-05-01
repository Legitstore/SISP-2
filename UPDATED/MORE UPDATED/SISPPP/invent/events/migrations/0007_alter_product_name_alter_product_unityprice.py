# Generated by Django 4.2.4 on 2023-09-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_product_unityprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('Milo', 'Milo'), ('Milk', 'Milk'), ('Kiwi', 'Kiwi'), ('Pizza', 'Pizza'), ('Avocado', 'Avocado'), ('Sandwich', 'Sandwich'), ('Strawberry', 'Strawberry'), ('Chicken Pie', 'Chicken Pie'), ('Strawberry Shake', 'Strawberry Shake')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unityprice',
            field=models.CharField(choices=[('400', '400 Milo'), ('500', '500 Milk'), ('300', '300 Kiwi'), ('900', '900 Pizza'), ('700', '700 Avocado'), ('850', '850 Sandwich'), ('600', '600 Strawberry'), ('450', '450 Chicken Pie'), ('500', '500 Strawberry  Shake')], max_length=100, null=True),
        ),
    ]
