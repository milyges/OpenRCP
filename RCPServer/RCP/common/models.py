from django.db import models
from django.contrib.auth.models import User
import datetime

class WorkDay(models.Model):
    name = models.TextField(verbose_name = 'Nazwa', max_length = 64)
    isFlexible = models.BooleanField('Nienormowany czas pracy', default = False)
    duration = models.DurationField(verbose_name = 'Dzień roboczy', default = datetime.timedelta(hours = 8)) 
    
class Person(models.Model):
    firstName = models.TextField(verbose_name = 'Imię', max_length = 64)
    lastName = models.TextField(verbose_name = 'Nazwisko', max_length = 64)
    isEmployed = models.BooleanField(verbose_name = 'Aktualnie zatrudniona', default = True)
    workDay = models.ForeignKey(WorkDay, verbose_name = 'Wymiar pracy', on_delete = models.CASCADE)
    user = models.OneToOneField(User, verbose_name = 'Powiązany użytkownik', on_delete = models.SET_NULL, blank = True, null = True)
    departament = models.ForeignKey('common.Departament', verbose_name = 'Dział', blank = True, null = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)
    
    class Meta:
        verbose_name = 'osoba'
        verbose_name_plural = 'osoby'

class Departament(models.Model):
    name = models.TextField(verbose_name = 'Nazwa', max_length = 64)
    managers = models.ManyToManyField(Person, verbose_name = 'Kierownicy', blank = True, related_name="departments_manager")
    