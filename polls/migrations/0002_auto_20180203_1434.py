# Generated by Django 2.0.2 on 2018-02-03 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chice',
            new_name='Choice',
        ),
    ]
