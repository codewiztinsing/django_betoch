# Generated by Django 4.1.4 on 2022-12-31 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_house_avgrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='oldPrice',
            field=models.DecimalField(decimal_places=2, default=144, max_digits=6),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.DecimalField(decimal_places=2, default=144, max_digits=6),
        ),
    ]
