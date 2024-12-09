from django.db import models

# Должности
class position(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.label

# Ученые степени
class academic_degree(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'

    def __str__(self):
        return self.label

# Преподаватели
class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    SURNAME = models.CharField(max_length=25, verbose_name='Фамилия')
    NAME = models.CharField(max_length=20, verbose_name='Имя')
    PATRONYMIC = models.CharField(max_length=20, verbose_name='Отчество')
    DATE_OF_BIRTH = models.DateField()
    email = models.CharField(max_length=24, verbose_name='Email')
    PHONE_NUMBER = models.CharField(max_length=20, verbose_name='Телефон')
    POSITION = models.OneToOneField(position, on_delete=models.CASCADE, verbose_name='Должность')
    ACADEMIC_DEGREE_ID = models.OneToOneField(academic_degree, on_delete=models.CASCADE, verbose_name='Ученая степень')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.PATRONYMIC

# Тип события
class event_type(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Тип мероприятия')

    class Meta:
        verbose_name = 'Тип мероприятия'
        verbose_name_plural = 'Типы мероприятий'

    def __str__(self):
        return self.label
    
# Студент
class student(models.Model):
    id = models.AutoField(primary_key=True)
    SURNAME = models.CharField(max_length=25, verbose_name='Фамилия')
    NAME = models.CharField(max_length=20, verbose_name='Имя')
    PATRONYMIC = models.CharField(max_length=20, verbose_name='Отчество')
    DATE_OF_BIRTH = models.DateField(verbose_name='Дата рождения')
    email = models.CharField(max_length=24, verbose_name='Email')
    PHONE_NUMBER = models.CharField(max_length=20, verbose_name='Телефон')
    SEX_TYPE = [
        ('man', 'мужчина'),
        ('woman', 'женщина'),
    ]
    SEX = models.CharField(max_length=10, choices=SEX_TYPE, verbose_name='Пол')
    ADDRESS = models.CharField(max_length=256, verbose_name='Адрес')
    DATE_START_STUDY = models.DateField(verbose_name='Дата начала обучения')

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'
    
    def __str__(self):
        return self.SURNAME

# Расписание
class schedule(models.Model):
    id = models.AutoField(primary_key=True)
    NOTE = models.CharField(max_length=256, verbose_name='Описание')
    TYPE = models.ForeignKey(event_type, on_delete=models.CASCADE, verbose_name='Тип события')
    TEACHER = models.OneToOneField(teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    VISITERS = models.ForeignKey(student, on_delete=models.CASCADE, verbose_name='Участники')
    DATE_EVENT = models.DateField(verbose_name='Дата мероприятия')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
    def __str__(self):
        return self.NOTE


# Код учебной программы или курса
class code_programm(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Код учебной программы'
        verbose_name_plural = 'Коды учебных программ'

    def __str__(self):
        return self.label

# Вид учебной дисциплины
class subject_classification(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Вид учебной дисциплины'
        verbose_name_plural = 'Виды учебных дисциплин'

    def __str__(self):
        return self.label
    
# Вид задания
class task_type(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Вид задания'
        verbose_name_plural = 'Виды заданий'

    def __str__(self):
        return self.label
    
# Задания
class task(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')
    DEADLINE = models.DateField(verbose_name='Срок сдачи')
    TYPE_ID = models.OneToOneField(task_type, on_delete=models.CASCADE, verbose_name='Тип работы')
    NOTE = models.CharField(max_length=255, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.NOTE

# Предмет
class subject(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')
    CLASSIFICATION = models.OneToOneField(subject_classification, on_delete=models.CASCADE, verbose_name='Тип дисциплины')
    TASKS = models.ForeignKey(task, on_delete=models.CASCADE, verbose_name='Задания')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.label


# Учебная программа
class education_programm(models.Model):
    id = models.AutoField(primary_key=True)
    CODE = models.OneToOneField(code_programm, on_delete=models.CASCADE, verbose_name='Код учебной программы')
    label = models.CharField(max_length=255, verbose_name='Наименование')
    SUBJECTS = models.ManyToManyField(subject, verbose_name='Предметы')
    
    class Meta:
        verbose_name = 'Учебная программа'
        verbose_name_plural = 'Учебная программа'
    
    def __str__(self):
        return self.label
    
# Статус выполнения задания
class status_check(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Статус выполнения задания'
        verbose_name_plural = 'Статусы выполнения заданий'

    def __str__(self):
        return self.label

# Результаты
class result_file(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Результат выполнения задания'
        verbose_name_plural = 'Результаты выполнения заданий'

    def __str__(self):
        return self.label

# Ведомость оценок 
class assessment_sheet(models.Model):
    id = models.AutoField(primary_key=True)
    EDUCATION_PROGRAMM  = models.OneToOneField(education_programm, on_delete=models.CASCADE, verbose_name='Код учебной программы')
    SUBJECT = models.OneToOneField(subject, on_delete=models.CASCADE, verbose_name='Предмет')
    TASK = models.OneToOneField(task, on_delete=models.CASCADE, verbose_name='Задание')
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE, verbose_name='Студент')
    RESULT = models.ForeignKey(result_file, on_delete=models.CASCADE, verbose_name='Результат', blank=True, null=True)
    STATUS_CHECK = models.ForeignKey(status_check, on_delete=models.CASCADE, verbose_name='Статус выполнения задания')
    COMMENT = models.CharField(max_length=256, verbose_name='Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Ведомость оценок'
        verbose_name_plural = 'Ведомость оценок'