# Generated by Django 3.0.5 on 2020-04-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Name')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('context', models.TextField(max_length=1000, verbose_name='Message')),
            ],
        ),
    ]
