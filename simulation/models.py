from django.db import models
from django.conf import settings


class Simulation(models.Model):    
    
    #NOTE: Entrees
    #vegetation
    limite_initiale_ox = models.FloatField(default=0.0)
    limite_finale_ox = models.FloatField(default=0.0)
    limite_initiale_oy = models.FloatField(default=0.0)
    limite_finale_oy = models.FloatField(default=0.0)
    longueur_de_la_flamme = models.FloatField(default=0.0)
    hauteur_de_la_végétation = models.FloatField(default=0.0)
    diametre_du_combustible = models.FloatField(default=0.0)
    densite_de_la_végétation  = models.FloatField(default=0.0)
    charge_surfacique_de_la_végétation = models.FloatField(default=0.0)
    teneur_en_eau_de_la_végétation = models.FloatField(default=0.0)
    temps_de_combustion =  models.FloatField(default=0.0)
    chaleur_spécifique_du_combustible = models.FloatField(default=0.0)
    coefficient_absorption_combustible = models.FloatField(default=0.0)
    emissivite_du_combustible = models.FloatField(default=0.0)


    #climat
    temps_de_simulation = models.FloatField(default=0.0)
    pas_de_temps = models.FloatField(default=0.0)
    pas_d_espace_ox = models.FloatField(default=0.0)
    pas_d_espace_oy = models.FloatField(default=0.0)
    temperature_ambiante = models.FloatField(default=0.0)
    vitesse_du_vent = models.FloatField(default=0.0)
    direction_du_vent = models.FloatField(default=0.0)
    pente_suivant_ox = models.FloatField(default=0.0)
    pente_suivant_oy = models.FloatField(default=0.0)
    temperature_de_la_flamme = models.FloatField(default=0.0)
    temperature_d_allumage = models.FloatField(default=0.0)
    temperature_des_braises = models.FloatField(default=0.0)
    emissivite_des_braises = models.FloatField(default=0.0)
    conductivite_des_braises = models.FloatField(default=0.0)
    conductivite_de_la_flamme = models.FloatField(default=0.0)
    viscosité_de_l_aire_chaud = models.FloatField(default=0.0)
    x_zone_de_calcul_initial = models.FloatField(default=0.0)
    x_zone_de_calcul_final = models.FloatField(default=0.0)
    y_zone_de_calcul_initial = models.FloatField(default=0.0)
    y_zone_de_calcul_final = models.FloatField(default=0.0)

    #eclosion
    coordonnées_x_depart_de_feu = models.FloatField(default=0.0)
    coordonnées_y_depart_de_feu = models.FloatField(default=0.0)
    cote_du_site_en_feu = models.CharField(max_length=10, default='')
    longueur_du_depart_de_feu = models.FloatField(default=0.0)
    temps_d_allumage = models.FloatField(default=0.0)
    abscisse_du_point_d_enregistrement = models.FloatField(default=0.0)
    ordonnée_du_point_d_enregistrement = models.FloatField(default=0.0) 

    #graphic
    graphic_urls = models.CharField(default='',max_length=10000)
    
    #common
    name = models.CharField(max_length=100)
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

