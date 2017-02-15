""" models """
from django.db import models

# Create your models here._


class VDay(models.Model):
    """ view v_day """
    view_id = models.CharField(max_length=17, primary_key=True)
    target = models.CharField(max_length=7)
    date = models.DateField()
    month = models.DecimalField(max_digits=2, decimal_places=0)
    week = models.DecimalField(max_digits=2, decimal_places=0)
    day = models.DecimalField(max_digits=2, decimal_places=0)
    open = models.DecimalField(max_digits=10, decimal_places=4)
    high = models.DecimalField(max_digits=10, decimal_places=4)
    low = models.DecimalField(max_digits=10, decimal_places=4)
    close = models.DecimalField(max_digits=10, decimal_places=4)
    ema12 = models.DecimalField(max_digits=10, decimal_places=4)
    ema26 = models.DecimalField(max_digits=10, decimal_places=4)
    pips = models.DecimalField(max_digits=11, decimal_places=4)
    pips_ratio = models.DecimalField(max_digits=19, decimal_places=8)

    class Meta:
        unique_together = (('target', 'date'))
        db_table = "v_day"


class VDayofweek(models.Model):
    """ view v_dayofweek """
    view_id = models.CharField(max_length=17, primary_key=True)
    target = models.CharField(max_length=7)
    date = models.DateField()
    dow = models.CharField(max_length=2)
    low = models.DecimalField(max_digits=10, decimal_places=4)
    high = models.DecimalField(max_digits=10, decimal_places=4)
    open = models.DecimalField(max_digits=10, decimal_places=4)
    close = models.DecimalField(max_digits=10, decimal_places=4)
    pips = models.DecimalField(max_digits=11, decimal_places=4)
    pips_ratio = models.DecimalField(max_digits=19, decimal_places=8)

    class Meta:
        unique_together = (('target', 'date'))
        db_table = "v_dayofweek"


class VWeek(models.Model):
    """ view v_week """
    view_id = models.CharField(max_length=17, primary_key=True)
    target = models.CharField(max_length=7)
    yyyy_week = models.CharField(max_length=7)
    week = models.DecimalField(max_digits=10, decimal_places=0)
    date_from = models.DateField()
    date_to = models.DateField()
    cnt = models.BigIntegerField()
    low = models.DecimalField(max_digits=10, decimal_places=4)
    high = models.DecimalField(max_digits=10, decimal_places=4)
    open = models.DecimalField(max_digits=10, decimal_places=4)
    close = models.DecimalField(max_digits=10, decimal_places=4)
    pips = models.DecimalField(max_digits=11, decimal_places=4)
    pips_ratio = models.DecimalField(max_digits=19, decimal_places=8)

    class Meta:
        unique_together = (('target', 'yyyy_week'))
        db_table = "v_week"


class VMonth(models.Model):
    """ view v_month """
    view_id = models.CharField(max_length=17, primary_key=True)
    target = models.CharField(max_length=7)
    yyyy_mm = models.CharField(max_length=7)
    mm = models.DecimalField(max_digits=10, decimal_places=0)
    date_from = models.DateField()
    date_to = models.DateField()
    cnt = models.BigIntegerField()
    low = models.DecimalField(max_digits=10, decimal_places=4)
    high = models.DecimalField(max_digits=10, decimal_places=4)
    open = models.DecimalField(max_digits=10, decimal_places=4)
    close = models.DecimalField(max_digits=10, decimal_places=4)
    pips = models.DecimalField(max_digits=11, decimal_places=4)
    pips_ratio = models.DecimalField(max_digits=19, decimal_places=8)

    class Meta:
        unique_together = (('target', 'yyyy_mm'))
        db_table = "v_month"
