# Generated by Django 4.2.4 on 2023-09-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_product_unityprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unityprice',
            field=models.CharField(choices=[('400', '400 ml'), ('500', '500 mk'), ('600', '600 sb'), ('500', '500 ssh'), ('700', '700 av'), ('300', '300 kw'), ('900', '900 pz'), ('450', '450 cp'), ('850', '850 sw')], max_length=100, null=True),
        ),
    ]
