from django.db import models
from app.models import Students

# Мероприятия
class Events(models.Model):
    name = models.CharField("Название", max_length=150)
    location = models.TextField("Место проведения")
    description = models.TextField("Описание")
    date = models.DateField("Дата проведения")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


# Студенты в мероприятиях
class StudentsInEvents(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="Студент", related_name="studentsInEvents")
    event = models.ForeignKey(Events, on_delete=models.CASCADE, verbose_name="Мероприятие", related_name="eventsForStudent")
    role = models.CharField("Роль студента в мероприятии", max_length=50, help_text="например, участник или победитель")
   
    def __str__(self):
        return f"{self.student}"

    class Meta:
        verbose_name = "Студенты в мероприятиях"
        verbose_name_plural = "Студенты в мероприятиях"



