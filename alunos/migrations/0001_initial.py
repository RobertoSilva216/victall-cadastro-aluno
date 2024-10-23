# Generated by Django 5.0.3 on 2024-10-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('matricula', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
