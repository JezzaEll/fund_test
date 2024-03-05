from django.db import models

# Create your models here.
class Fund(models.Model):
    name            = models.CharField(max_length=100)
    strategy        = models.CharField(max_length=50)
    aum             = models.IntegerField(blank=True, null=True)
    inception_date  = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'fund'
        ordering = ['name',]
        verbose_name_plural = "Funds"
    
    def __str__(self):
        return self.name
