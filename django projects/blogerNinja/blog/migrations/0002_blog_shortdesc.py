# Generated by Django 3.0.14 on 2022-05-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='shortdesc',
            field=models.CharField(default='', max_length=300),
        ),
    ]