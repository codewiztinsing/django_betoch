# Generated by Django 4.1.4 on 2023-01-14 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_image_alter_listing_image_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image_5',
        ),
    ]