from django.db import models
from django.contrib.auth.models import User


# Form #1  Entry condition

class EntryConditionModel(models.Model):
    field_1 = models.CharField(
        max_length=100,
        verbose_name='Select Field'
    )  # {"time","day", "MA_Cross","BB","ST","M_ACD",'pattern_no"}

    class Meta:
        verbose_name_plural = 'Entry Conditions Field #1 '
        verbose_name = 'Entry Conditions Field #1'

    def __str__(self):
        return f"{self.field_1}"


class EntryConditionLevel_1(models.Model):
    level_1 = models.ForeignKey(
        EntryConditionModel,
        on_delete=models.CASCADE, # verbose_name = '',
    )
    option = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Entry Condition Level #1'
        verbose_name = 'Entry Condition Level #1'

    def __str__(self):
        return f"{self.level_1} | {self.option}"


class EntryConditionLevel_2(models.Model):
    level_2 = models.ForeignKey(
        EntryConditionModel,
        on_delete=models.CASCADE,  # verbose_name = ''
    )
    CondOption = models.CharField(
        max_length=100,
        # verbose_name = ''
    )

    class Meta:
        verbose_name_plural = 'Entry Condition Level #2'
        verbose_name = 'Entry Condition Level #2'

    def __str__(self):
        return f"{self.level_2} | {self.CondOption}"


class EntryConditionField_2(models.Model):
    condition = models.CharField(
        max_length=100,
        # verbose_name= ''
    )

    class Meta:
        verbose_name_plural = 'Entry Conditions Field #2 '
        verbose_name = 'Entry Conditions Field #2 '

    def __str__(self):
        return f"Entry Condition :- {self.condition}"


class EntryConditionField_3(models.Model):
    field_1 = models.ForeignKey(
        EntryConditionModel,
        on_delete = models.CASCADE,
        # verbose_name = '',
    )
    variable = models.CharField(
        max_length=100,
        # verbose_name = '',
    )

    class Meta:
        verbose_name_plural = 'Entry Conditions Field #3'
        verbose_name = 'Entry Conditions Field #3'

    def __str__(self):
        return f"Entry Condition Form {self.field_1} | {self.variable}"


class TrailConditionModel(models.Model):
    field_1 = models.CharField(
        max_length=100,
        # verbose_name = ''
    )  # {same as entry condition for addition of profit and risk_value}
    field_2 = models.CharField(
        max_length=100,
        verbose_name = '',
    )  # {"less_than_equal_to","less_than","equal_to","greater_than","greater_than_equal_to"}

    class Meta:
        verbose_name_plural = 'Trail Condition Field #1 '
        verbose_name = 'Trail Condition Field #1'

    def __str__(self):
        return f"{self.field_1}"


class TrailConditionLevel_1(models.Model):
    field_1 = models.ForeignKey(
        TrailConditionModel,
        on_delete=models.CASCADE,
        # verbose_name='',
    )
    option = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Trail Condition Level #1'
        verbose_name = 'Trail Condition Level #1'

    def __str__(self):
        return f"{self.field_1} | {self.option}"


class RiskManagementModel(models.Model):
    field_1 = models.CharField(
        max_length=50,
        # verbose_name=''
    )

    class Meta:
        verbose_name_plural = 'Risk Management Condition'
        verbose_name = 'Risk Management Condition'

    def __str__(self):
        return f"{self.field_1}"
