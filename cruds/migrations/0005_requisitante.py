# Generated by Django 2.1.4 on 2018-12-23 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0004_fornecedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('observacoes', models.TextField()),
                ('idDepartamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cruds.Departamento')),
            ],
        ),
    ]