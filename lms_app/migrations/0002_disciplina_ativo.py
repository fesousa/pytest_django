# Generated by Django 2.0.4 on 2018-04-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]