# Generated by Django 3.0.5 on 2020-04-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20200424_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ecom1',
            field=models.URLField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='ecom2',
            field=models.URLField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='ecom3',
            field=models.URLField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='unboxing',
            field=models.URLField(default='', max_length=250),
        ),
    ]
