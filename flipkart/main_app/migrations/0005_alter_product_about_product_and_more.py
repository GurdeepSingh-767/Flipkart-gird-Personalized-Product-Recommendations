# Generated by Django 4.1.10 on 2023-08-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_product_review_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='about_product',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='review_content',
            field=models.CharField(max_length=300),
        ),
    ]
