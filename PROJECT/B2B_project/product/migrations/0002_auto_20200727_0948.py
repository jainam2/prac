# Generated by Django 3.0.6 on 2020-07-27 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller_profile'),
        ),
    ]