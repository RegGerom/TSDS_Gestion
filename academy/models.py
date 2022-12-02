from django.db import models


class Career(models.Model):
    career_pk = models.AutoField(primary_key=True)
    career_list = [
        ('NOSEL', 'Sin seleccionar'),
        ('TSDS', 'Tecnicatura Superior de Diseño de Software'),
        ('TSSAE', 'Tecnicatura Superior en Secretariado Administrativo Escolar')
    ]    
    name = models.CharField(max_length=5, choices=career_list, default='NOSEL')
    duration = models.PositiveSmallIntegerField(default=3)

    def __str__(self) -> str:
        return f"{self.name} {self.duration}"


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    birth = models.DateField()
    sex_list = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sex = models.CharField(max_length=1, choices=sex_list, default='F')
    career = models.ForeignKey(Career, null=False, blank=False, on_delete=models.CASCADE)
    year_list = [('1', '1ro'), ('2', '2do'), ('3', '3ro')]
    year = models.CharField(max_length=1, choices=year_list, default='1')
    liability_list = [
        ('Libre', 'Libre'),
        ('Cursando', 'Cursando')
    ]
    liability = models.CharField(max_length=8, choices=liability_list, default='Cursando')

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.career} {self.year} {self.dni} {self.birth} {self.sex} {self.liability}"


class Subject(models.Model):
    #subject_id = models.AutoField(primary_key=True)
    subject_list = [
        ('01', 'Matemática'),
        ('02', 'Etica'),
        ('03', 'Filosofía'),
        ('04', 'Sis. Op.'),
        ('05', 'Dis. Sistemas'),
        ('06', 'Taller Inf.'),
        ('07', 'Redes Com.'),
        ('08', 'Bases de Datos'),
        ('09', 'Inn. y Des.'),
        ('10', 'Inglés Tec I'),
        ('11', 'Inglés Tec II'),
        ('12', 'Lóg. Est. Datos')
    ]
    subject_name = models.CharField(max_length=2, choices=subject_list, default='01')

    def __str__(self) -> str:
        return f"{self.subject_name}"


class SubjectByStudent(models.Model):
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    name = models.ForeignKey(Subject, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return f"{self.student} {self.name} {self.date}"


        
    