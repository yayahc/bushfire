from django.db import models
from django.conf import settings


class X1veg(models.Model):
    x1veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.x1veg
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "X1veg"
        verbose_name = "X1veg"
        verbose_name_plural = "X1vegs"
        
class X2veg(models.Model):
    x2veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.x2veg
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "X2veg"
        verbose_name = "X2veg"
        verbose_name_plural = "X2vegs"
    
class Y1veg(models.Model):
    y1veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.y1veg
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "Y1veg"
        verbose_name = "Y1veg"
        verbose_name_plural = "Y1vegs"
    
class Y2veg(models.Model):
    y2veg = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.y2veg
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "Y2veg"
        verbose_name = "Y2veg"
        verbose_name_plural = "Y2vegs"
    
class TeneurEnEau(models.Model):
    teneur_en_eau = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teneur_en_eau
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "TeneurEnEau"
        verbose_name = "TeneurEnEau"
        verbose_name_plural = "TeneurEnEaus"

class HauteurFuelBed(models.Model):
    hauteur_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hauteur_fuel_bed
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "HauteurFuelBed"
        verbose_name = "HauteurFuelBed"
        verbose_name_plural = "HauteurFuelBeds"
    
class EmissiviteFuelBed(models.Model):
    emissivite_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emissivite_fuel_bed
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "EmissiviteFuelBed"
        verbose_name = "EmissiviteFuelBed"
        verbose_name_plural = "EmissiviteFuelBeds"
    
class AbsorptionFuelBed(models.Model):
    absorption_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.absorption_fuel_bed
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "AbsorptionFuelBed"
        verbose_name = "AbsorptionFuelBed"
        verbose_name_plural = "AbsorptionFuelBeds"
    
class FractionVolumiq(models.Model):
    fraction_volumiq = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fraction_volumiq
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "FractionVolumiq"
        verbose_name = "FractionVolumiq"
        verbose_name_plural = "FractionVolumiqs"
    
class DensiteFuelBed(models.Model):
    densite_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.densite_fuel_bed
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "DensiteFuelBed"
        verbose_name = "DensiteFuelBed"
        verbose_name_plural = "DensiteFuelBeds"

class SurfaceSpec(models.Model):
    surface_spec = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.surface_spec
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "SurfaceSpec"
        verbose_name = "SurfaceSpec"
        verbose_name_plural = "SurfaceSpecs"
            
class DiametreFuelBed(models.Model):
    diametre_fuel_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.diametre_fuel_bed
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "DiametreFuelBed"
        verbose_name = "DiametreFuelBed"
        verbose_name_plural = "DiametreFuelBeds"
    
class ChaleurSpecFeulBed(models.Model):
    chaleur_spec_feul_bed = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chaleur_spec_feul_bed
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "ChaleurSpecFeulBed"
        verbose_name = "ChaleurSpecFeulBed"
        verbose_name_plural = "ChaleurSpecFeulBeds"
    
class ChargeSurface(models.Model):
    charge_surface = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.charge_surface
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "ChargeSurface"
        verbose_name = "ChargeSurface"
        verbose_name_plural = "ChargeSurfaces"
    
class HauteurFlamme(models.Model):
    hauteur_flamme = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hauteur_flamme
    
    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "HauteurFlamme"
        verbose_name = "HauteurFlamme"
        verbose_name_plural = "HauteurFlammes"

class TimeCombustion(models.Model):
    time_combustion = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.time_combustion

    class Meta:
        """
        Meta Information
        """        
        app_label = "simulation"
        db_table = "TimeCombustion"
        verbose_name = "TimeCombustion"
        verbose_name_plural = "TimeCombustions"


class Simulation(models.Model):    
    
    #NOTE: Entrees

    #Vegetation
    typeVegetation = models.IntegerField(default=0)
    nbrDepartFeu = models.IntegerField(default=0)
    timp = models.IntegerField(default=0)
    x1veg = models.FloatField(default=0.0)
    x2veg = models.FloatField(default=0.0)
    y1veg = models.FloatField(default=0.0)
    y2veg = models.FloatField(default=0.0)
    hauteurFlamme = models.FloatField(default=0.0)
    hauteurFuelBed = models.FloatField(default=0.0)
    diametreFuelBed = models.FloatField(default=0.0)
    densiteFuelBed = models.FloatField(default=0.0)
    chargeSurface = models.FloatField(default=0.0)
    teneurEnEau = models.FloatField(default=0.0)
    timeCombustion = models.FloatField(default=0.0)
    chaleurSpecFeulBed = models.FloatField(default=0.0)
    absorptionFuelBed = models.FloatField(default=0.0)
    emissiviteFuelBed = models.FloatField(default=0.0)

    #Climat
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
    timeMax = models.FloatField(default=0.0)
    deltat = models.FloatField(default=0.0)
    deltax = models.FloatField(default=0.0)
    deltay = models.FloatField(default=0.0)
    xDebut = models.FloatField(default=0.0)
    xFin = models.FloatField(default=0.0)
    yDebut = models.FloatField(default=0.0)
    yFin = models.FloatField(default=0.0)
    
    #Depart feu
    nbEclosion = models.IntegerField(default=0)
    xEclosion = models.FloatField(default=0.0)
    yEclosion = models.FloatField(default=0.0)
    coteSiteFeu = models.CharField(default='', max_length=10)
    timeAllumage = models.FloatField(default=0.0)
    xenreg = models.FloatField(default=0.0)
    yenreg = models.FloatField(default=0.0)
    longueurEclosion = models.FloatField(default=0.0)
    
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

