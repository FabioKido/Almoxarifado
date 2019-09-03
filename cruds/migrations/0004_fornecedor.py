# Generated by Django 2.1.4 on 2018-12-23 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0003_departamento_endereco_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaoSocial', models.CharField(max_length=50)),
                ('nomeFantasia', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('dataRegistro', models.DateField()),
                ('observacoes', models.TextField()),
                ('idEndereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cruds.Endereco')),
                ('idTelefone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cruds.Telefone')),
            ],
        ),
    ]