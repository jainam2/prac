# Generated by Django 3.0.6 on 2020-07-27 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('product_img', models.ImageField(upload_to='')),
                ('mrp', models.FloatField(default=0.0)),
                ('wsp', models.FloatField(default=0.0)),
                ('rating', models.FloatField(default=0.0)),
                ('category', models.CharField(default='', max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('COD', models.BooleanField(default=True)),
                ('favourite', models.BooleanField(default=True)),
                ('seller_info', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='seller.seller_profile')),
            ],
        ),
    ]
