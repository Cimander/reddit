# Generated by Django 4.2.7 on 2024-04-11 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicate', '0003_remove_cart_post_alter_post_category_cart_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
