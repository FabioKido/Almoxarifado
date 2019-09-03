# Generated by Django 2.1.4 on 2018-12-23 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0005_requisitante'),
        ('registros', '0002_recepcaomateriais'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisicaoMateriais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataRegistro', models.DateField()),
                ('condicao', models.CharField(max_length=10)),
                ('observacoes', models.TextField()),
                ('idRequisitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cruds.Requisitante')),
            ],
        ),
    ]