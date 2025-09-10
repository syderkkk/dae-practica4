from django.db import models
from django.urls import reverse

class Student(models.Model):
    CAREER_CHOICES = [
        ('sistemas', 'Sistemas de Información'),
        ('software', 'Desarrollo de Software'),
        ('redes', 'Redes y Comunicaciones'),
        ('industrial', 'Ingeniería Industrial'),
        ('mecanica', 'Ingeniería Mecánica'),
    ]
    
    SEMESTER_CHOICES = [
        (1, 'Primer Semestre'),
        (2, 'Segundo Semestre'),
        (3, 'Tercer Semestre'),
        (4, 'Cuarto Semestre'),
        (5, 'Quinto Semestre'),
        (6, 'Sexto Semestre'),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    student_id = models.CharField(max_length=10, unique=True, verbose_name="Código de Estudiante")
    career = models.CharField(max_length=20, choices=CAREER_CHOICES, verbose_name="Carrera")
    semester = models.IntegerField(choices=SEMESTER_CHOICES, verbose_name="Semestre")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name} - {self.student_id}"

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"