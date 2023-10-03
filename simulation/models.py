from django.db import models
from django.conf import settings


class X1veg(models.Model):
    x1veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.x1veg
        
class X2veg(models.Model):
    x2veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.x2veg
    
class Y1veg(models.Model):
    y1veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.y1veg
    
class Y2veg(models.Model):
    y2veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.y2veg
    
class TeneurEnEau(models.Model):
    teneur_en_eau = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teneur_en_eau

class HauteurFuelBed(models.Model):
    hauteur_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hauteur_fuel_bed
    
class EmissiviteFuelBed(models.Model):
    emissivite_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emissivite_fuel_bed
    
class AbsorptionFuelBed(models.Model):
    absorption_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.absorption_fuel_bed
    
class FractionVolumiq(models.Model):
    fraction_volumiq = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fraction_volumiq
    
class DensiteFuelBed(models.Model):
    densite_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.densite_fuel_bed

class SurfaceSpec(models.Model):
    surface_spec = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.surface_spec
            
class DiametreFuelBed(models.Model):
    diametre_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.diametre_fuel_bed
    
class ChaleurSpecFeulBed(models.Model):
    chaleur_spec_feul_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chaleur_spec_feul_bed
    
class ChargeSurface(models.Model):
    charge_surface = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.charge_surface
    
class HauteurFlamme(models.Model):
    hauteur_flamme = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hauteur_flamme

class TimeCombustion(models.Model):
    time_combustion = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.time_combustion


class Simulation(models.Model):    
    
    #NOTE: Entrees
    timp = models.FloatField(default=0.0)
    typeVegetation = models.IntegerField(default=0)
    x1veg = models.ForeignKey(X1veg, on_delete=models.CASCADE, null=True)
    x2veg = models.ForeignKey(X2veg, on_delete=models.CASCADE, null=True)
    y1veg = models.ForeignKey(Y1veg, on_delete=models.CASCADE, null=True)
    y2veg = models.ForeignKey(Y2veg, on_delete=models.CASCADE, null=True)
    teneurEnEau = models.ForeignKey(TeneurEnEau, on_delete=models.CASCADE, null=True)
    hauteurFuelBed = models.ForeignKey(HauteurFuelBed, on_delete=models.CASCADE, null=True)
    emissiviteFuelBed = models.ForeignKey(EmissiviteFuelBed, on_delete=models.CASCADE, null=True)
    absorptionFuelBed = models.ForeignKey(AbsorptionFuelBed, on_delete=models.CASCADE, null=True)
    densiteFuelBed = models.ForeignKey(DensiteFuelBed, on_delete=models.CASCADE, null=True)
    diametreFuelBed = models.ForeignKey(DiametreFuelBed, on_delete=models.CASCADE, null=True)
    chaleurSpecFeulBed = models.ForeignKey(ChaleurSpecFeulBed, on_delete=models.CASCADE, null=True)
    chargeSurface = models.ForeignKey(ChargeSurface, on_delete=models.CASCADE, null=True)
    hauteurFlamme = models.ForeignKey(HauteurFlamme, on_delete=models.CASCADE, null=True)
    timeCombustion = models.ForeignKey(TimeCombustion, on_delete=models.CASCADE, null=True)
    timeMax = models.FloatField(default=0.0)
    deltat = models.FloatField(default=0.0)
    deltax = models.FloatField(default=0.0)
    deltay = models.FloatField(default=0.0)
    xDebut = models.FloatField(default=0.0)
    xFin = models.FloatField(default=0.0)
    yDebut = models.FloatField(default=0.0)
    yFin = models.FloatField(default=0.0)
    temperatureAir = models.FloatField(default=0.0)
    vitesseDuVent = models.FloatField(default=0.0)
    directionDuVen = models.FloatField(default=0.0)
    pentex = models.FloatField(default=0.0)
    pentey = models.FloatField(default=0.0)
    temperatureFlamme = models.FloatField(default=0.0)
    temperatureAllumage = models.FloatField(default=0.0)
    temperatureBrais = models.FloatField(default=0.0)
    emissiviteBraise = models.FloatField(default=0.0)
    conductiviteBraise = models.FloatField(default=0.0)
    conductiviteFlamme = models.FloatField(default=0.0)
    viscositeAirChau = models.FloatField(default=0.0)
    nbEclosion = models.IntegerField(default=0)
    xEclosion = models.FloatField(default=0.0)
    yEclosion = models.FloatField(default=0.0)
    timeAllumage = models.FloatField(default=0.0)
    longueurEclosion = models.FloatField(default=0.0)
    xenreg = models.FloatField(default=0.0)
    yenreg = models.FloatField(default=0.0)
    
    #graphic
    graphic_urls = models.CharField(default='',max_length=10000)
    
    #common
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, default='')
    ville = models.CharField(max_length=100, default='')

    #auto-generated
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

