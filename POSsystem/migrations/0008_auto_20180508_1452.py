# Generated by Django 2.0.4 on 2018-05-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSsystem', '0007_auto_20180508_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POSsystem.Item'),
        ),
    ]