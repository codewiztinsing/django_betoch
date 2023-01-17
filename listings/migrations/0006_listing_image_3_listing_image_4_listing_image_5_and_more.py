# Generated by Django 4.1.4 on 2023-01-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_listing_image_3_remove_listing_image_4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_5',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bath_rooms',
            field=models.IntegerField(default=0),
        ),
    ]
