from django.db import models
from django.contrib.auth.models import User
#Create your models here

"""
# Form #1  Entry condition
class EntryConditionModel(models.Model):
    field1 = models.CharField(max_length=100) #  {"time","day", "MA_Cross","BB","ST","MACD",'pattern_no"}
    field3 = models.CharField(max_length=100) #  {"less_than_equal_to","less_than","equal_to","greater_than","greater_than_equal_to"}

    class Meta:
        verbose_name_plural = '#1 FIELDS'
        verbose_name = '#1 FIELD'

    def __str__(self):
        return f"{self.field1}"



class EntryConditionOptions(models.Model):
    field1 = models.ForeignKey(EntryConditionModel, on_delete=models.CASCADE,)
    option = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Options for field1'
        verbose_name = 'Option for field1'

    def __str__(self):
        return f"{self.field1} | {self.option}"


class EntryCasCondition(models.Model):
    field1 = models.ForeignKey(EntryConditionModel, on_delete=models.CASCADE,)
    CondOption =  models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '#4 Field Conditions'
        verbose_name = '#4 Field Conditions'

    def __str__(self):
        return f"{self.field1} | {CondOption}"



class EntryCondition(models.Model):


    class Meta:
        verbose_name_plural = 'PLURAL_NAME'
        verbose_name = 'NaME'

    def __str__(self):
        return
"""