# Generated by Django 4.2.7 on 2024-03-12 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicate', '0025_remove_comment_author_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
