# Generated by Django 4.0.3 on 2022-04-06 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_variantmodel_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VariantModel',
            new_name='Variant',
        ),
    ]
