from django.db import models
from app.models import Students

# Проекты
class Projects(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    dateStart = models.DateField("Дата начала работы над проектом")
    dateEnd = models.DateField("Дата окончания работ над проектом")
    links = models.TextField("Список ссылок")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

# Команды
class Teams(models.Model):
    name = models.CharField("Название", max_length=150)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="Проект", related_name="teamsForProject")
    participants = models.ManyToManyField(
        Students, verbose_name="Участники", related_name="studentsForTeam", null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.project}"

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

