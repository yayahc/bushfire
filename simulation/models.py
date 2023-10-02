from django.db import models
from django.conf import settings


class Simulation(models.Model):    
    
    #entrees
    name = models.CharField(max_length=100)
    x = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    y = models.DecimalField(max_digits=10, decimal_places=6, default=0) 

    #graphic
    graphic_urls = models.CharField(default='',max_length=10000)
    
    #common
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="simulation")

    class Meta:
        """
        Meta Information
        """
        app_label = "simulation"
        db_table = "simulations"
        verbose_name = "simulation"
        verbose_name_plural = "simulations"

    def __str__(self):
        return self.name

