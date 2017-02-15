from django.db import models

# Create your models here.
class VDay(models.Model):
    target = models.CharField(max_length=7)
    date = models.DateField()
    day = models.DecimalField(max_digits=2,decimal_places=0)
    low = models.DecimalField(max_digits=10,decimal_places=4)
    high = models.DecimalField(max_digits=10,decimal_places=4)
    open = models.DecimalField(max_digits=10,decimal_places=4)
    close = models.DecimalField(max_digits=10,decimal_places=4)
    pips =  models.DecimalField(max_digits=11,decimal_places=4)
    pips_ratio = models.DecimalField(max_digits=19,decimal_places=8)
    
    class Meta:
        unique_together = (('target','date'))
        db_table = "v_day"