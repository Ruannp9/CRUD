# Generated by Django 5.1.2 on 2024-10-31 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time_Futebol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_time', models.CharField(max_length=200)),
                ('tecnico_time', models.CharField(max_length=200)),
                ('data_criacao', models.DateField()),
                ('Mascote', models.CharField(max_length=200)),
                ('quantidade_titulos', models.IntegerField()),
            ],
        ),
    ]
