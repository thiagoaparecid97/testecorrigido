# Generated by Django 2.0.3 on 2018-04-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=128)),
                ('complemento', models.CharField(max_length=256, null=True)),
                ('uf', models.CharField(max_length=2, null=True)),
                ('cidade', models.CharField(max_length=64, null=True)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
    ]
