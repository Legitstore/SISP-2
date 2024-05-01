# Generated by Django 4.2.4 on 2023-09-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_product_unityprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unityprice',
            field=models.CharField(choices=[('ML 400', 'ML 400'), ('MK 500', 'MK 500 '), ('STB 600', 'SB 600'), ('SBS 500', 'SSH 500'), ('AV 700', 'AV 700'), ('KW 300', 'KW 300'), ('PZ 900', 'PZ 900'), ('CP 450', 'CP 450'), ('SW 850', 'SW 850')], max_length=100, null=True),
        ),
    ]