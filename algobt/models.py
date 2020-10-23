from django.db import models
from django.contrib.auth.models import User
#Create your models here

class EntryConditionModel(models.model):
    field1 = models.CharField(max_length=100) #  {"time","day", "MA_Cross","BB","ST","MACD",'pattern_no"}
    field3 = models.CharField(max_length=100) #  {"less_than_equal_to","less_than","equal_to","greater_than","greater_than_equal_to"}

    class Meta:
        verbose_name_plural = '#1 FIELDS'
        verbose_name = '#1 FIELD'
    def __str__(self):
        return f"{self.field1}"


class EntryConditionOptions(models.model):
    field1 = models.ForeignKey(EntryCondition, on_delete=models.CASCADE,)
    option = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Options for field1'
        verbose_name = 'Option for field1'

    def __str__(self):
        return f"{self.field1} | {self.option}"


class EntryCasCondition(models.model):
    field1 = models.ForeignKey(EntryCondition, on_delete=models.CASCADE,)
    CondOption =  models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '#4 Field Condotions'
        verbose_name = '#4 Field Condotions'

    def __str__(self):
        return f"{self.field1} | {}"


class EntryCondition(models.model):


    class Meta:
        verbose_name_plural =
        verbose_name =

    def __str__(self):
        return
