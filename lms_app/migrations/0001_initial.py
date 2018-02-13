# Generated by Django 2.0.2 on 2018-02-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=9)),
                ('ra', models.IntegerField()),
                ('desconto', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('carga_horaria', models.IntegerField()),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=9)),
                ('ra', models.IntegerField()),
                ('disciplinas', models.ManyToManyField(to='lms_app.Disciplina')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to='lms_app.Disciplina'),
        ),
    ]