# Generated by Django 4.1.10 on 2023-08-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_user_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50, unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('rating_count', models.IntegerField()),
                ('about_product', models.TextField()),
                ('review_id', models.IntegerField()),
                ('review_title', models.CharField(max_length=200)),
                ('review_content', models.TextField()),
                ('img_link', models.URLField()),
            ],
        ),
    ]
