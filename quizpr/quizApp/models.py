from django.db import models


# Create your models here.
class Quiz(models.Model):
    name = models.CharField('Название квиза', max_length=255, default='')

    def __str__(self):
        return self.name


class Cost(models.Model):
    description = models.CharField('Описание типа ценности ответа', max_length=255, default='')

    def __str__(self):
        return self.description


class EventState(models.Model):
    description = models.CharField('Состояние события', max_length=255, default='')

    def __str__(self):
        return self.description


class Tour(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    num = models.IntegerField('Номер тура в квизе', default=0)
    subject = models.CharField('Тема тура', max_length=255)
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.quiz.name + "/" + self.subject


class AnswerType(models.Model):
    description = models.CharField('Описание типа вопроса', max_length=255, default='')

    def __str__(self):
        return self.description


class Question(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    number = models.IntegerField('Номер вопроса в туре', default=0)
    answer_type = models.ForeignKey(AnswerType, on_delete=models.CASCADE)
    correct = models.CharField('Правильный ответ', max_length=1000, default='')
    description = models.CharField('Описание', max_length=255, default='', blank=True)

    def __str__(self):
        res = str(self.tour.subject) + "_" + str(self.number)
        return res


class Event(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    location = models.CharField('Место проведения квиза', max_length=255)
    date = models.DateField('Дата проведения квиза', default='1970-01-01')
    event_state = models.ForeignKey(EventState, on_delete=models.CASCADE)
    # 1 - Don't started
    # 2 - Going
    # 3 - Ended

    def __str__(self, *args, **kwargs):
        res = str(self.location) + " " + str(self.date)
        return res

    def save(self, *args, **kwargs):
        going = EventState.objects.get(description='Идёт')
        ended = EventState.objects.get(description='Закончилось')
        if self.event_state == going:
            for event in Event.objects.filter(event_state=going):
                if event != self:
                    event.event_state = ended
                    event.save()
        stages = Stage.objects.filter(event=self.id)
        if len(stages) == 0:
            for tour in Tour.objects.filter(quiz=self.quiz):
                stage = Stage(event=self, tour=tour)
                # stage.event = self
                # stage.tour = tour
                stage.save()
        super(Event, self).save(*args, **kwargs)


class Stage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, blank=True)
    time_start = models.DateTimeField('Время начала тура', default=None, blank=True, null=True)
    time_stop = models.DateTimeField('время конца тура', default=None, blank=True, null=True)


class Team(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)
    sid = models.CharField('Идентификатор сессии', max_length=32)
    name = models.CharField('Название команды', max_length=255, default='')
    slogan = models.CharField('Девиз команды', max_length=255, default='')

    def __str__(self):
        return self.name


class Answer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True)
    cost = models.IntegerField('Ставка', default=0, blank=True)
    answer = models.CharField('Ответ команды', max_length=1000, default='')
    correct = models.BooleanField('Правильный ли был ответ', default='')
