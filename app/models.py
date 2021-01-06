from django.db import models

# Университеты
class Universities(models.Model):
    fullname = models.CharField("Полное название", max_length=150)
    shortname = models.CharField("Краткое название или аббревиатура", max_length=100)
    location = models.CharField("Город", max_length=150)
    description = models.TextField("Описание")
    phone = models.CharField("Телефон", max_length=50)
    
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"

# Факультеты
class Faculties(models.Model):
    name = models.CharField("Название факультета", max_length=150)
    description = models.TextField("Описание")
    university = models.ForeignKey(Universities, on_delete=models.CASCADE, verbose_name="Университет", related_name="facultiesOfUniversity")
    
    def __str__(self):
        return f"{self.name} - {self.university}"

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

# Специальности
class Specializations(models.Model):
    codeName = models.CharField("Код специальности", max_length=50)
    name = models.CharField("Название специальности", max_length=150)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE, verbose_name="Факультет", related_name="specializationsOfFaculty")
    
    def __str__(self):
        return f"{self.codeName} - {self.name}"

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

# Группы
class Groups(models.Model):
    codeName = models.CharField("Номер группы", max_length=50)
    specialization = models.ForeignKey(Specializations, on_delete=models.CASCADE, verbose_name="Специальность", related_name="groupsOfSpecialization")
    course = models.PositiveIntegerField("Курс")
    formEducation = models.CharField("Форма обучения", max_length=100, help_text="(очная/заочная/очно-заочная)")
    studyDegree = models.CharField("Ступень высшего образования", max_length=160, help_text="например, бакалавриат")
    
    def __str__(self):
        return f"{self.codeName}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


# Студенты
class Students(models.Model):
    fullname = models.CharField("ФИО", max_length=160)
    birthdate = models.DateField("Дата рождения")
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True, verbose_name="Группа", related_name="studentsOfGroup")
    phone = models.CharField("Телефон", max_length=50)
    email = models.EmailField("Email")
    budgetary = models.BooleanField("Бюджетное обучение", default=False)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

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
        Students, verbose_name="Участники", related_name="studentsForTeam")

    def __str__(self):
        return f"{self.name} - {self.project}"

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"



