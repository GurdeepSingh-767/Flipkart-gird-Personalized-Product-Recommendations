# Generated by Django 4.1.10 on 2023-08-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review_id',
            field=models.CharField(max_length=50),
        ),
    ]
