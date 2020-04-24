# Generated by Django 3.0.5 on 2020-04-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_contac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='ecom1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='ecom2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='ecom3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='feat',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='unboxing',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contac',
            name='context',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contac',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contac',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
