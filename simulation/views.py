from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import UserRegistrationForm
from .models import AbsorptionFuelBed, ChaleurSpecFeulBed, ChargeSurface, DensiteFuelBed, DiametreFuelBed, EmissiviteFuelBed, HauteurFlamme, HauteurFuelBed, Simulation, TeneurEnEau, TimeCombustion, X1veg, X2veg, Y1veg, Y2veg
from django.http import HttpResponse
from .forms import UploadSimulationForm

import re
import os
import csv
import matplotlib.pyplot as plt
from django.conf import settings

from .drawer import main_draw


def drawer(x, y, title):

    #NOTE : create the simulation directory
    urls = ''
    simulation_dir = os.path.join('media', title)
    os.makedirs(simulation_dir, exist_ok=True)

    for i in range(4):
        c = i + 1
        plt.figure()
        plt.plot(x, y) 
        plt.xlabel('X Value')
        plt.ylabel('Y Value')
        plt.title(f'2D Plot for Simulation {title} - Figure {i + 1}')
        plt.grid(True)

        plt.xlim(0, 20) 
        plt.ylim(0, 20) 

        plt.plot([c, x+c], [c, y+c], linestyle='--', color='red', label='Intersection (0,0)')
        plt.plot([0, x+c], [0, y+c], linestyle='--', color='green', label='Intersection (0,0)')


    #NOTE : update URLs and save PNG
    file_name = f'simulation_{title}_2d_plot_{i + 1}.png'
    urls += f'{file_name}|'
    file_path = os.path.join(simulation_dir, file_name)
    plt.savefig(file_path)

    plt.close()

    return urls



@login_required
def simulations(request):
    if request.method == 'POST':
        
        #NOTE: Get Entrees
        timp = request.POST.get('timp')
        typeVegetation = request.POST.get('typeVegetation')
        nbrDepartFeu = request.POST.get('nbrDepartFeu')

        x1veg = request.POST.get('x1veg')
        x2veg = x2veg = request.POST.get('x2veg')        
        y1veg = request.POST.get('y1veg')
        y2veg = request.POST.get('y2veg')
        teneurEnEau = request.POST.get('teneurEnEau')        
        hauteurFuelBed = request.POST.get('hauteurFuelBed')        
        emissiviteFuelBed = request.POST.get('emissiviteFuelBed')
        absorptionFuelBed = request.POST.get('absorptionFuelBed')
        densiteFuelBed = request.POST.get('densiteFuelBed')        
        diametreFuelBed = request.POST.get('diametreFuelBed')        
        chaleurSpecFeulBed = request.POST.get('chaleurSpecFeulBed')        
        chargeSurface = request.POST.get('chargeSurface')        
        hauteurFlamme = request.POST.get('hauteurFlamme')        
        timeCombustion = request.POST.get('timeCombustion')        
        timeMax = request.POST.get('timeMax')
        deltat = request.POST.get('deltat')
        deltax = request.POST.get('deltax')
        deltay = request.POST.get('deltay')
        xDebut = request.POST.get('xDebut')
        xFin = request.POST.get('xFin')
        yDebut = request.POST.get('yDebut')
        yFin = request.POST.get('yFin')
        temperatureAir = request.POST.get('temperatureAir')
        vitesseDuVent = request.POST.get('vitesseDuVent')
        directionDuVen = request.POST.get('directionDuVen')
        pentex = request.POST.get('pentex')
        pentey = request.POST.get('pentey')
        temperatureFlamme = request.POST.get('temperatureFlamme')
        temperatureAllumage = request.POST.get('temperatureAllumage')
        temperatureBrais = request.POST.get('temperatureBrais')
        emissiviteBraise = request.POST.get('emissiviteBraise')
        conductiviteBraise = request.POST.get('conductiviteBraise')
        conductiviteFlamme = request.POST.get('conductiviteFlamme')
        viscositeAirChau = request.POST.get('viscositeAirChau')
        nbEclosion = request.POST.get('nbEclosion')
        xEclosion = request.POST.get('xEclosion')
        yEclosion = request.POST.get('yEclosion')
        coteSiteFeu = request.POST.get('coteSiteFeu')
        timeAllumage = request.POST.get('timeAllumage')
        longueurEclosion = request.POST.get('longueurEclosion')
        xenreg = request.POST.get('xenreg')
        yenreg = request.POST.get('yenreg')
        
        #common
        name = request.POST.get('name')
        region = request.POST.get('region')
        ville = request.POST.get("ville")

        #TODO: build right drawer
        # simulation_graphic_urls = drawer(float(limite_initiale_ox),float(limite_initiale_oy), simulation_name)

        simulation = Simulation.objects.create(
            timp = timp,
            typeVegetation = typeVegetation,
            nbrDepartFeu = nbrDepartFeu,
            x1veg = x1veg,
            x2veg = x2veg,
            y1veg = y1veg,
            y2veg = y2veg,
            teneurEnEau = teneurEnEau,
            hauteurFuelBed = hauteurFuelBed,
            emissiviteFuelBed = emissiviteFuelBed,
            absorptionFuelBed = absorptionFuelBed,
            densiteFuelBed = densiteFuelBed,
            diametreFuelBed = diametreFuelBed,
            chaleurSpecFeulBed = chaleurSpecFeulBed,
            chargeSurface = chargeSurface,
            hauteurFlamme = hauteurFlamme,
            timeCombustion = timeCombustion,
            timeMax = timeMax,
            deltat = deltat,
            deltax = deltax,
            deltay = deltay,
            xDebut = xDebut,
            xFin = xFin,
            yDebut = yDebut,
            yFin = yFin,
            temperatureAir = temperatureAir,
            vitesseDuVent = vitesseDuVent,
            directionDuVen = directionDuVen,
            pentex = pentex,
            pentey = pentey,
            temperatureFlamme = temperatureFlamme,
            temperatureAllumage = temperatureAllumage,
            temperatureBrais = temperatureBrais,
            emissiviteBraise = emissiviteBraise,
            conductiviteBraise = conductiviteBraise,
            conductiviteFlamme = conductiviteFlamme,
            viscositeAirChau = viscositeAirChau,
            nbEclosion = nbEclosion,
            xEclosion = xEclosion,
            yEclosion = yEclosion,
            coteSiteFeu = coteSiteFeu,
            timeAllumage = timeAllumage,
            longueurEclosion = longueurEclosion,
            xenreg = xenreg,
            yenreg = yenreg,
            graphic_urls = "",
            name = name,
            region = region,
            ville = ville,
            user=request.user,
        )

        #NOTE : Create csv files and txt file
        write_vegetation_csv(simulation)
        write_climat_csv(simulation)
        write_eclosion_csv(simulation)
        write_contour_txt(simulation)

        return redirect("simulations")

    simulations = Simulation.objects.order_by("-id")

    # pagination 4 items per page
    paginator = Paginator(simulations, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"simulations": simulations, "page_obj": page_obj}
    return render(request, "simulation/simulations.html", context)



def update_simulation(request, pk):
    simulation = get_object_or_404(Simulation, id=pk, user=request.user)
    if request.method == 'POST':

        #NOTE: get datas
        new_simulation_name = request.POST.get(f"name_{pk}")

        #vegetation
        new_limite_initiale_ox = request.POST.get(f"limite_initiale_ox_{pk}")
        new_limite_finale_ox = request.POST.get(f"limite_finale_ox_{pk}")
        new_limite_initiale_oy = request.POST.get(f"limite_initiale_oy_{pk}")
        new_limite_finale_oy = request.POST.get(f"limite_finale_oy_{pk}")
        new_longueur_de_la_flamme = request.POST.get(f"longueur_de_la_flamme_{pk}")
        new_hauteur_de_la_végétation = request.POST.get(f"hauteur_de_la_végétation_{pk}")
        new_diametre_du_combustible = request.POST.get(f"diametre_du_combustible_{pk}")
        new_densite_de_la_végétation  =request.POST.get(f"densite_de_la_végétation_{pk}")
        new_charge_surfacique_de_la_végétation = request.POST.get(f"charge_surfacique_de_la_végétation_{pk}")
        new_teneur_en_eau_de_la_végétation = request.POST.get(f"teneur_en_eau_de_la_végétation_{pk}")
        new_temps_de_combustion = request.POST.get(f"temps_de_combustion_{pk}")
        new_chaleur_spécifique_du_combustible = request.POST.get(f"chaleur_spécifique_du_combustible_{pk}")
        new_coefficient_absorption_combustible = request.POST.get(f"coefficient_absorption_combustible_{pk}")
        new_emissivite_du_combustible = request.POST.get(f"emissivite_du_combustible_{pk}")
    
        #climat
        new_temps_de_simulation = request.POST.get(f"temps_de_simulation_{pk}")
        new_pas_de_temps = request.POST.get(f"pas_de_temps_{pk}")
        new_pas_d_espace_ox = request.POST.get(f"pas_d_espace_ox_{pk}")
        new_pas_d_espace_oy = request.POST.get(f"pas_d_espace_oy_{pk}")
        new_temperature_ambiante = request.POST.get(f"temperature_ambiante_{pk}")
        new_vitesse_du_vent = request.POST.get(f"vitesse_du_vent_{pk}")
        new_direction_du_vent = request.POST.get(f"direction_du_vent_{pk}")
        new_pente_suivant_ox = request.POST.get(f"pente_suivant_ox_{pk}")
        new_pente_suivant_oy = request.POST.get(f"pente_suivant_oy_{pk}")
        new_temperature_de_la_flamme = request.POST.get(f"temperature_de_la_flamme_{pk}")
        new_temperature_d_allumage = request.POST.get(f"temperature_d_allumage_{pk}")
        new_temperature_des_braises = request.POST.get(f"temperature_des_braises_{pk}")
        new_emissivite_des_braises = request.POST.get(f"emissivite_des_braises_{pk}")
        new_conductivite_des_braises = request.POST.get(f"conductivite_des_braises_{pk}")
        new_conductivite_de_la_flamme = request.POST.get(f"conductivite_de_la_flamme_{pk}")
        new_viscosité_de_l_aire_chaud = request.POST.get(f"viscosité_de_l_aire_chaud_{pk}")
        new_x_zone_de_calcul_initial = request.POST.get(f"x_zone_de_calcul_initial_{pk}")
        new_x_zone_de_calcul_final = request.POST.get(f"x_zone_de_calcul_final_{pk}")
        new_y_zone_de_calcul_initial = request.POST.get(f"y_zone_de_calcul_initial_{pk}")
        new_y_zone_de_calcul_final = request.POST.get(f"y_zone_de_calcul_final_{pk}")
    
        #eclosion
        new_coordonnées_x_depart_de_feu = request.POST.get(f"coordonnées_x_depart_de_feu_{pk}") 
        new_coordonnées_y_depart_de_feu = request.POST.get(f"coordonnées_y_depart_de_feu_{pk}") 
        new_cote_du_site_en_feu = request.POST.get(f"cote_du_site_en_feu_{pk}")
        new_longueur_du_depart_de_feu = request.POST.get(f"longueur_du_depart_de_feu_{pk}") 
        new_temps_d_allumage = request.POST.get(f"temps_d_allumage_{pk}") 
        new_abscisse_du_point_d_enregistrement = request.POST.get(f"abscisse_du_point_d_enregistrement_{pk}") 
        new_ordonnée_du_point_d_enregistrement = request.POST.get(f"ordonnée_du_point_d_enregistrement_{pk}") 


        #NOTE : update
        simulation.name = new_simulation_name
        simulation.limite_initiale_ox = new_limite_initiale_ox
        simulation.limite_finale_ox = new_limite_finale_ox
        simulation.limite_initiale_oy = new_limite_initiale_oy
        simulation.limite_finale_oy = new_limite_finale_oy
        simulation.longueur_de_la_flamme = new_longueur_de_la_flamme
        simulation.hauteur_de_la_végétation = new_hauteur_de_la_végétation
        simulation.diametre_du_combustible = new_diametre_du_combustible
        simulation.densite_de_la_végétation = new_densite_de_la_végétation
        simulation.charge_surfacique_de_la_végétation = new_charge_surfacique_de_la_végétation
        simulation.teneur_en_eau_de_la_végétation = new_teneur_en_eau_de_la_végétation
        simulation.temps_de_combustion = new_temps_de_combustion
        simulation.chaleur_spécifique_du_combustible = new_chaleur_spécifique_du_combustible
        simulation.coefficient_absorption_combustible = new_coefficient_absorption_combustible
        simulation.emissivite_du_combustible = new_emissivite_du_combustible

        simulation.temps_de_simulation= new_temps_de_simulation
        simulation.pas_de_temps= new_pas_de_temps
        simulation.pas_d_espace_ox= new_pas_d_espace_ox
        simulation.pas_d_espace_oy= new_pas_d_espace_oy
        simulation.temperature_ambiante= new_temperature_ambiante
        simulation.vitesse_du_vent= new_vitesse_du_vent
        simulation.direction_du_vent= new_direction_du_vent
        simulation.pente_suivant_ox= new_pente_suivant_ox
        simulation.pente_suivant_oy= new_pente_suivant_oy
        simulation.temperature_de_la_flamme= new_temperature_de_la_flamme
        simulation.temperature_d_allumage= new_temperature_d_allumage
        simulation.temperature_des_braises= new_temperature_des_braises
        simulation.emissivite_des_braises= new_emissivite_des_braises
        simulation.conductivite_des_braises= new_conductivite_des_braises
        simulation.conductivite_de_la_flamme= new_conductivite_de_la_flamme
        simulation.viscosité_de_l_aire_chaud= new_viscosité_de_l_aire_chaud
        simulation.x_zone_de_calcul_initial= new_x_zone_de_calcul_initial
        simulation.x_zone_de_calcul_final= new_x_zone_de_calcul_final
        simulation.y_zone_de_calcul_initial= new_y_zone_de_calcul_initial
        simulation.y_zone_de_calcul_final= new_y_zone_de_calcul_final

        simulation.coordonnées_x_depart_de_feu = new_coordonnées_x_depart_de_feu
        simulation.coordonnées_y_depart_de_feu = new_coordonnées_y_depart_de_feu
        simulation.cote_du_site_en_feu = new_cote_du_site_en_feu
        simulation.longueur_du_depart_de_feu = new_longueur_du_depart_de_feu
        simulation.temps_d_allumage = new_temps_d_allumage
        simulation.abscisse_du_point_d_enregistrement = new_abscisse_du_point_d_enregistrement
        simulation.ordonnée_du_point_d_enregistrement = new_ordonnée_du_point_d_enregistrement

        #TODO: build right drawer
        simulation.graphic_urls = drawer(float(new_limite_initiale_ox),float(new_limite_initiale_oy), new_simulation_name)

        simulation.save()
        return render(request, 'simulation/simulation_detail.html', {'simulation': simulation})
    
    simulation = get_object_or_404(Simulation, pk=pk)
    return render(request, 'simulation/simulation_edit.html', {'simulation': simulation})



def new_simulation(request):
    return render(request, 'simulation/simulation_new.html')


def detail_simulation(request,pk):
    simulation = get_object_or_404(Simulation, pk=pk)
    return render(request, 'simulation/simulation_detail.html', {'simulation': simulation})

def register(request):
    """
    User Registration form

    Args:
        request (POST): New user registered
    """    
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "simulation/register.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")
    

def complete_simulation(request, pk):
    simulation = get_object_or_404(Simulation, id=pk, user=request.user)
    simulation.is_completed = True
    simulation.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_simulation(request, pk):    
    simulation = get_object_or_404(Simulation, id=pk, user=request.user)
    simulation.delete()
    return redirect("simulations")


def write_vegetation_csv(simulation):    
    #NOTE: VEGETATION
    # Define the file path where the CSV will be stored
    simulation_dir = os.path.join(settings.MEDIA_ROOT, simulation.name)
    os.makedirs(simulation_dir, exist_ok=True)
    csv_file_path = os.path.join(simulation_dir, 'vegetation.csv')
    
    # Create and write the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['variables', 'valeurs'])
        writer.writerow(['x1veg',simulation.x1veg])
        writer.writerow(['x2veg',simulation.x2veg])
        writer.writerow(['y1veg',simulation.y1veg])
        writer.writerow(['y2veg',simulation.y2veg])
        writer.writerow(['hauteurFlamme',simulation.hauteurFlamme])
        writer.writerow(['hauteurFuelBed',simulation.hauteurFuelBed])
        writer.writerow(['diametreFuelBed',simulation.diametreFuelBed])
        writer.writerow(['densiteFuelBed',simulation.densiteFuelBed])        
        writer.writerow(['chargeSurface',simulation.chargeSurface])
        writer.writerow(['teneurEnEau',simulation.teneurEnEau])
        writer.writerow(['timeCombustion',simulation.timeCombustion])
        writer.writerow(['chaleurSpecFeulBed',simulation.chaleurSpecFeulBed])
        writer.writerow(['absorptionFuelBed',simulation.absorptionFuelBed])
        writer.writerow(['emissiviteBraise',simulation.emissiviteBraise])
    
     # Return a response indicating the file location
    response = HttpResponse("CSV file saved successfully.", content_type='text/plain')
    return response


def write_climat_csv(simulation):
    #NOTE: CLIMAT
    # Define the file path where the CSV will be stored
    simulation_dir = os.path.join(settings.MEDIA_ROOT, simulation.name)
    os.makedirs(simulation_dir, exist_ok=True)
    csv_file_path = os.path.join(simulation_dir, 'climat.csv')
    
    # Create and write the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['variables', 'valeurs'])
        writer.writerow(['timeMax',simulation.timeMax])
        writer.writerow(['deltat',simulation.deltat])
        writer.writerow(['deltax',simulation.deltax])
        writer.writerow(['deltay',simulation.deltay])
        writer.writerow(['xDebut',simulation.xDebut])
        writer.writerow(['xFin',simulation.xFin])
        writer.writerow(['yDebut',simulation.yDebut])
        writer.writerow(['yFin',simulation.yFin])
        writer.writerow(['temperatureAir',simulation.temperatureAir])
        writer.writerow(['vitesseDuVent',simulation.vitesseDuVent])
        writer.writerow(['directionDuVen',simulation.directionDuVen])
        writer.writerow(['pentex',simulation.pentex])
        writer.writerow(['pentey',simulation.pentey])
        writer.writerow(['temperatureFlamme',simulation.temperatureFlamme])
        writer.writerow(['temperatureAllumage',simulation.temperatureAllumage])
        writer.writerow(['temperatureBrais',simulation.temperatureBrais])
        writer.writerow(['emissiviteBraise',simulation.emissiviteBraise])
        writer.writerow(['conductiviteBraise',simulation.conductiviteBraise])
        writer.writerow(['conductiviteFlamme',simulation.conductiviteFlamme])
        writer.writerow(['viscositeAirChau',simulation.viscositeAirChau])
    
     # Return a response indicating the file location
    response = HttpResponse("CSV file saved successfully.", content_type='text/plain')
    return response


def write_eclosion_csv(simulation):
    #NOTE: ECLOSION
    # Define the file path where the CSV will be stored
    simulation_dir = os.path.join(settings.MEDIA_ROOT, simulation.name)
    csv_file_path = os.path.join(simulation_dir, 'eclosion.csv')
    
    # Create and write the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['variables', 'valeurs'])
        writer.writerow(['xEclosion',simulation.yEclosion])
        writer.writerow(['yEclosion',simulation.yEclosion])
        writer.writerow(['coteSiteFeu',simulation.coteSiteFeu])
        writer.writerow(['longueurEclosion',simulation.longueurEclosion])
        writer.writerow(['timeAllumage',simulation.timeAllumage])
        writer.writerow(['xenreg',simulation.xenreg])
        writer.writerow(['xenreg',simulation.xenreg])
    
     # Return a response indicating the file location
    response = HttpResponse("CSV file saved successfully.", content_type='text/plain')
    return response


def write_contour_txt(simulation):
    #NOTE: ECLOSION
    # Define the file path where the CSV will be stored
    simulation_dir = os.path.join(settings.MEDIA_ROOT, simulation.name)
    txt_file_path = os.path.join(simulation_dir, 'contour.txt')

    with open(txt_file_path, 'w') as txtfile:
        txtfile.write(f"Simulation Name: {simulation.name}\n")
        txtfile.write(f"Created On: {simulation.created_on}\n")
        txtfile.write(f"Updated On: {simulation.updated_on}\n")
        txtfile.write(f"User: {simulation.user}\n")

    # Return a response indicating the file location
    response = HttpResponse("TXT file saved successfully.", content_type='text/plain')
    return response


def download_vegetation(simulation):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="vegetation.csv"'

    # vegetation
    writer = csv.writer(response)
    writer.writerow([simulation.x1veg])
    writer.writerow([simulation.x2veg])
    writer.writerow([simulation.y1veg])
    writer.writerow([simulation.y2veg])
    writer.writerow([simulation.hauteurFlamme])
    writer.writerow([simulation.hauteurFuelBed])
    writer.writerow([simulation.diametreFuelBed])
    writer.writerow([simulation.chargeSurface])
    writer.writerow([simulation.teneurEnEau])
    writer.writerow([simulation.timeCombustion])
    writer.writerow([simulation.chaleurSpecFeulBed])
    writer.writerow([simulation.absorptionFuelBed])
    writer.writerow([simulation.emissiviteBraise])

    return response
    
def download_climat(simulation):   

    responseTwo = HttpResponse(content_type='text/csv')
    responseTwo['Content-Disposition'] = f'attachment; filename="vegetation.csv"'
    #climat
    writer = csv.writer(responseTwo)
    writer.writerow([simulation.timeMax])
    writer.writerow([simulation.timeMax])
    writer.writerow([simulation.deltat])
    writer.writerow([simulation.deltax])
    writer.writerow([simulation.deltay])
    writer.writerow([simulation.xDebut])
    writer.writerow([simulation.xFin])
    writer.writerow([simulation.yDebut])
    writer.writerow([simulation.yFin])
    writer.writerow([simulation.temperatureAir])
    writer.writerow([simulation.vitesseDuVent])
    writer.writerow([simulation.directionDuVen])
    writer.writerow([simulation.pentex])
    writer.writerow([simulation.pentey])
    writer.writerow([simulation.temperatureFlamme])
    writer.writerow([simulation.temperatureAllumage])
    writer.writerow([simulation.temperatureBrais])
    writer.writerow([simulation.emissiviteBraise])
    writer.writerow([simulation.conductiviteBraise])
    writer.writerow([simulation.conductiviteFlamme])
    writer.writerow([simulation.viscositeAirChau])

def download_eclosion(simulation):
    #eclosion
    responseThree = HttpResponse(content_type='text/csv')
    responseThree['Content-Disposition'] = f'attachment; filename="vegetation.csv"'
    writer = csv.writer(responseThree)
    writer.writerow([simulation.xEclosion])
    writer.writerow([simulation.yEclosion])
    writer.writerow([simulation.yEclosion])
    writer.writerow(['centre'])
    writer.writerow([simulation.timeAllumage])
    writer.writerow([simulation.xenreg])
    writer.writerow([simulation.xenreg])



def download_all_simulations(request):
    simulations = Simulation.objects.all()

    content = ""
    for simulation in simulations:
        content += f"Simulation Name: {simulation.name}\n"
        content += f"Created On: {simulation.created_on}\n"
        content += f"Updated On: {simulation.updated_on}\n"
        content += f"User: {simulation.user}\n"
        content += "\n\n\n\n\n\n"

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="all_simulations.txt"'
    return response


# @login_required
# def upload_simulation(request):
#     if request.method == 'POST':
#         form = UploadSimulationForm(request.POST, request.FILES)

#         if form.is_valid():
#             txt_file = form.cleaned_data['txt_file']
#             content = txt_file.read().decode('utf-8')
            
#             name = re.search(r'Simulation Name: (.+)', content)
#             created_on_match = re.search(r'Created On: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
#             updated_on_match = re.search(r'Updated On: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
#             x = re.search(r'X: (\d+\.\d+)', content)
#             y = re.search(r'Y: (\d+\.\d+)', content)
#             user_match = re.search(r'User: (\w+)', content)

#             if created_on_match and updated_on_match and user_match and x and y and name:
#                 name = name.group(1)
#                 created_on = created_on_match.group(1)
#                 updated_on = updated_on_match.group(1)
#                 x = float(x.group(1))
#                 y = float(y.group(1))
#                 user = user_match.group(1)

#                 simulation = Simulation.objects.create(
#                     name=name,
#                     created_on=created_on,
#                     updated_on=updated_on,
#                     x=x,
#                     y=y,
#                     user=request.user,
#                 )

#                 return redirect('simulations')

#     else:
#         form = UploadSimulationForm()

#     return render(request, 'simulation/upload_simulation.html', {'form': form})


def simulate(request, pk):    
    simulation = get_object_or_404(Simulation, pk=pk)
    main_draw(simulation.timp,simulation.nbEclosion,simulation.typeVegetation,simulation.name)



def view_graphic(request, pk):
    simulation = get_object_or_404(Simulation, pk=pk)
    
    # Specify the directory path
    directory_path = f"media/{simulation.name}/images" 

    # Initialize a list to store the image paths
    # image_paths = ''

    # Loop through the files in the directory
    # for filename in os.listdir(directory_path):
    #     if filename.endswith(".png"):
    #         # Check if the file has a .png extension
    #         image_path = os.path.join(directory_path, filename)
    #         image_paths += image_path+'|'

    # urls = image_array
    urls = directory_path
    print(urls)
    return render(request, 'simulation/graphic_detail.html', {'simulation': simulation, 'urls':urls})
