# Generated by Django 2.0.3 on 2018-04-01 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('eventoPrincipal', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('dataEHoraDeInicio', models.DateField(max_length=10)),
                ('palavrasChaves', models.CharField(max_length=100)),
                ('logotipo', models.CharField(max_length=10)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evento.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cpf', models.CharField(max_length=12)),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.AddField(
            model_name='eventos',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evento.Pessoa'),
        ),
    ]