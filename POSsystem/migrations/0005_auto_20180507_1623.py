# Generated by Django 2.0.4 on 2018-05-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSsystem', '0004_category_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
