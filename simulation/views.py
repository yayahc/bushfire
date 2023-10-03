from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import UserRegistrationForm
from .models import Simulation
from django.http import HttpResponse
from .forms import UploadSimulationForm

import re
import os
import csv
import matplotlib.pyplot as plt


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

        #NOTE: get datas
        simulation_name = request.POST.get("name")

        #vegetation
        limite_initiale_ox = request.POST.get("limite_initiale_ox")
        limite_finale_ox = request.POST.get("limite_finale_ox")
        limite_initiale_oy = request.POST.get("limite_initiale_oy")
        limite_finale_oy = request.POST.get("limite_finale_oy")
        longueur_de_la_flamme = request.POST.get("longueur_de_la_flamme")
        hauteur_de_la_végétation = request.POST.get("hauteur_de_la_végétation")
        diametre_du_combustible = request.POST.get("diametre_du_combustible")
        densite_de_la_végétation  =request.POST.get("densite_de_la_végétation")
        charge_surfacique_de_la_végétation = request.POST.get("charge_surfacique_de_la_végétation")
        teneur_en_eau_de_la_végétation = request.POST.get("teneur_en_eau_de_la_végétation")
        temps_de_combustion = request.POST.get("temps_de_combustion")
        chaleur_spécifique_du_combustible = request.POST.get("chaleur_spécifique_du_combustible")
        coefficient_absorption_combustible = request.POST.get("coefficient_absorption_combustible")
        emissivite_du_combustible = request.POST.get("emissivite_du_combustible")
    
    
        #climat
        temps_de_simulation = request.POST.get("temps_de_simulation")
        pas_de_temps = request.POST.get("pas_de_temps")
        pas_d_espace_ox = request.POST.get("pas_d_espace_ox")
        pas_d_espace_oy = request.POST.get("pas_d_espace_oy")
        temperature_ambiante = request.POST.get("temperature_ambiante")
        vitesse_du_vent = request.POST.get("vitesse_du_vent")
        direction_du_vent = request.POST.get("direction_du_vent")
        pente_suivant_ox = request.POST.get("pente_suivant_ox")
        pente_suivant_oy = request.POST.get("pente_suivant_oy")
        temperature_de_la_flamme = request.POST.get("temperature_de_la_flamme")
        temperature_d_allumage = request.POST.get("temperature_d_allumage")
        temperature_des_braises = request.POST.get("temperature_des_braises")
        emissivite_des_braises = request.POST.get("emissivite_des_braises")
        conductivite_des_braises = request.POST.get("conductivite_des_braises")
        conductivite_de_la_flamme = request.POST.get("conductivite_de_la_flamme")
        viscosité_de_l_aire_chaud = request.POST.get("viscosité_de_l_aire_chaud")
        x_zone_de_calcul_initial = request.POST.get("x_zone_de_calcul_initial")
        x_zone_de_calcul_final = request.POST.get("x_zone_de_calcul_final")
        y_zone_de_calcul_initial = request.POST.get("y_zone_de_calcul_initial")
        y_zone_de_calcul_final = request.POST.get("y_zone_de_calcul_final")
    
        #eclosion
        coordonnées_x_depart_de_feu = request.POST.get("coordonnées_x_depart_de_feu") 
        coordonnées_y_depart_de_feu = request.POST.get("coordonnées_y_depart_de_feu") 
        cote_du_site_en_feu = request.POST.get("cote_du_site_en_feu")
        longueur_du_depart_de_feu = request.POST.get("longueur_du_depart_de_feu") 
        temps_d_allumage = request.POST.get("temps_d_allumage") 
        abscisse_du_point_d_enregistrement = request.POST.get("abscisse_du_point_d_enregistrement") 
        ordonnée_du_point_d_enregistrement = request.POST.get("ordonnée_du_point_d_enregistrement")  

        #TODO: build right drawer
        simulation_graphic_urls = drawer(float(limite_initiale_ox),float(limite_initiale_oy), simulation_name)

        simulation = Simulation.objects.create(
            name=simulation_name,
            limite_initiale_ox = limite_initiale_ox,
            limite_finale_ox = limite_finale_ox,
            limite_initiale_oy = limite_initiale_oy,
            limite_finale_oy = limite_finale_oy,
            longueur_de_la_flamme = longueur_de_la_flamme,
            hauteur_de_la_végétation = hauteur_de_la_végétation,
            diametre_du_combustible = diametre_du_combustible,
            densite_de_la_végétation = densite_de_la_végétation,
            charge_surfacique_de_la_végétation = charge_surfacique_de_la_végétation,
            teneur_en_eau_de_la_végétation = teneur_en_eau_de_la_végétation,
            temps_de_combustion = temps_de_combustion,
            chaleur_spécifique_du_combustible = chaleur_spécifique_du_combustible,
            coefficient_absorption_combustible = coefficient_absorption_combustible,
            emissivite_du_combustible = emissivite_du_combustible,
            temps_de_simulation = temps_de_simulation,
            pas_de_temps = pas_de_temps,
            pas_d_espace_ox = pas_d_espace_ox,
            pas_d_espace_oy = pas_d_espace_oy,
            temperature_ambiante = temperature_ambiante,
            vitesse_du_vent = vitesse_du_vent,
            direction_du_vent = direction_du_vent,
            pente_suivant_ox = pente_suivant_ox,
            pente_suivant_oy = pente_suivant_oy,
            temperature_de_la_flamme = temperature_de_la_flamme,
            temperature_d_allumage = temperature_d_allumage,
            temperature_des_braises = temperature_des_braises,
            emissivite_des_braises = emissivite_des_braises,
            conductivite_des_braises = conductivite_des_braises,
            conductivite_de_la_flamme = conductivite_de_la_flamme,
            viscosité_de_l_aire_chaud = viscosité_de_l_aire_chaud,
            x_zone_de_calcul_initial = x_zone_de_calcul_initial,
            x_zone_de_calcul_final = x_zone_de_calcul_final,
            y_zone_de_calcul_initial = y_zone_de_calcul_initial,
            y_zone_de_calcul_final = y_zone_de_calcul_final,
            coordonnées_x_depart_de_feu = coordonnées_x_depart_de_feu,
            coordonnées_y_depart_de_feu = coordonnées_y_depart_de_feu,
            cote_du_site_en_feu = cote_du_site_en_feu,
            longueur_du_depart_de_feu = longueur_du_depart_de_feu,
            temps_d_allumage = temps_d_allumage,
            abscisse_du_point_d_enregistrement = abscisse_du_point_d_enregistrement,
            ordonnée_du_point_d_enregistrement = ordonnée_du_point_d_enregistrement,
            user=request.user,
            graphic_urls=simulation_graphic_urls
        )

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


def download_simulation(request, pk):
    simulation = get_object_or_404(Simulation, pk=pk)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{simulation.name}.csv"'

    # Create a CSV writer and write simulation data
    writer = csv.writer(response)
    writer.writerow(['Simulation Name', simulation.name])
    writer.writerow(['Created On', simulation.created_on])
    writer.writerow(['Updated On', simulation.updated_on])
    writer.writerow(['User', simulation.user.username])

    return response


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


def view_graphic(request, pk):    
    simulation = get_object_or_404(Simulation, pk=pk)

    image_array = simulation.graphic_urls.split('|')
    if image_array[-1] == '':
        image_array.pop()

    urls = image_array
    return render(request, 'simulation/graphic_detail.html', {'simulation': simulation, 'urls':urls})
