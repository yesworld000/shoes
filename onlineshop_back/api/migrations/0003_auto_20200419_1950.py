# Generated by Django 3.0.4 on 2020-04-19 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200407_2326'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gender',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='gender',
            new_name='category',
        ),
    ]