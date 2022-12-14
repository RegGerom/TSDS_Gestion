# Generated by Django 4.1.3 on 2022-12-02 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('career_pk', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('NOSEL', 'Sin seleccionar'), ('TSDS', 'Tecnicatura Superior de Diseño de Software'), ('TSSAE', 'Tecnicatura Superior en Secretariado Administrativo Escolar')], default='NOSEL', max_length=5)),
                ('duration', models.PositiveSmallIntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
                ('birth', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('year', models.CharField(choices=[('1', '1ro'), ('2', '2do'), ('3', '3ro')], default='1', max_length=1)),
                ('liability', models.CharField(choices=[('Libre', 'Libre'), ('Cursando', 'Cursando')], default='Cursando', max_length=8)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.career')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(choices=[('01', 'Matemática'), ('02', 'Etica'), ('03', 'Filosofía'), ('04', 'Sis. Op.'), ('05', 'Dis. Sistemas'), ('06', 'Taller Inf.'), ('07', 'Redes Com.'), ('08', 'Bases de Datos'), ('09', 'Inn. y Des.'), ('10', 'Inglés Tec I'), ('11', 'Inglés Tec II'), ('12', 'Lóg. Est. Datos')], default='01', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectByStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.subject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.student')),
            ],
        ),
    ]
