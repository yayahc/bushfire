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


def simulations(request):
    simulations = Simulation.objects.order_by("-id")

    # pagination 4 items per page
    paginator = Paginator(simulations, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"simulations": simulations, "page_obj": page_obj}
    return render(request, "simulation/simulations.html", context)


@login_required
def new_simulation(request):
    if request.method == 'POST':
        
        #NOTE: Get Entries
        timp = request.POST.get('timp')
        typeVegetation = request.POST.get('typeVegetation')
        nbrDepartFeu = request.POST.get('nbrDepartFeu')

        x1veg = request.POST.get('x1veg')
        x2veg = request.POST.get('x2veg')        
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

        return redirect("detail_simulation", pk=simulation.pk)

    simulation = Simulation.objects
    return render(request, "simulation/simulation_new.html")


def all_simmulations(request):
    simulations = Simulation.objects.order_by("-id")
    return render(request, "simulation/all_simulations.html", {"simulations":simulations})
    

def update_simulation(request, pk):
    simulation = get_object_or_404(Simulation, id=pk, user=request.user)
    if request.method == 'POST':

        #NOTE: Get Entries
        new_timp = request.POST.get(f'timp{pk}')
        new_typeVegetation = request.POST.get(f'typeVegetation{pk}')
        new_nbrDepartFeu = request.POST.get(f'nbrDepartFeu{pk}')

        new_x1veg = request.POST.get(f'x1veg{pk}')
        new_x2veg = request.POST.get(f'x2veg{pk}')
        new_y1veg = request.POST.get(f'y1veg{pk}')
        new_y2veg = request.POST.get(f'y2veg{pk}')
        new_teneurEnEau = request.POST.get(f'teneurEnEau{pk}')
        new_hauteurFuelBed = request.POST.get(f'hauteurFuelBed{pk}')
        new_emissiviteFuelBed = request.POST.get(f'emissiviteFuelBed{pk}')
        new_absorptionFuelBed = request.POST.get(f'absorptionFuelBed{pk}')
        new_densiteFuelBed = request.POST.get(f'densiteFuelBed{pk}')
        new_diametreFuelBed = request.POST.get(f'diametreFuelBed{pk}')
        new_chaleurSpecFeulBed = request.POST.get(f'chaleurSpecFeulBed{pk}')
        new_chargeSurface = request.POST.get(f'chargeSurface{pk}')
        new_hauteurFlamme = request.POST.get(f'hauteurFlamme{pk}')
        new_timeCombustion = request.POST.get(f'timeCombustion{pk}')
        new_timeMax = request.POST.get(f'timeMax{pk}')
        new_deltat = request.POST.get(f'deltat{pk}')
        new_deltax = request.POST.get(f'deltax{pk}')
        new_deltay = request.POST.get(f'deltay{pk}')
        new_xDebut = request.POST.get(f'xDebut{pk}')
        new_xFin = request.POST.get(f'xFin{pk}')
        new_yDebut = request.POST.get(f'yDebut{pk}')
        new_yFin = request.POST.get(f'yFin{pk}')
        new_temperatureAir = request.POST.get(f'temperatureAir{pk}')
        new_vitesseDuVent = request.POST.get(f'vitesseDuVent{pk}')
        new_directionDuVen = request.POST.get(f'directionDuVen{pk}')
        new_pentex = request.POST.get(f'pentex{pk}')
        new_pentey = request.POST.get(f'pentey{pk}')
        new_temperatureFlamme = request.POST.get(f'temperatureFlamme{pk}')
        new_temperatureAllumage = request.POST.get(f'temperatureAllumage{pk}')
        new_temperatureBrais = request.POST.get(f'temperatureBrais{pk}')
        new_emissiviteBraise = request.POST.get(f'emissiviteBraise{pk}')
        new_conductiviteBraise = request.POST.get(f'conductiviteBraise{pk}')
        new_conductiviteFlamme = request.POST.get(f'conductiviteFlamme{pk}')
        new_viscositeAirChau = request.POST.get(f'viscositeAirChau{pk}')
        new_nbEclosion = request.POST.get(f'nbEclosion{pk}')
        new_xEclosion = request.POST.get(f'xEclosion{pk}')
        new_yEclosion = request.POST.get(f'yEclosion{pk}')
        new_coteSiteFeu = request.POST.get(f'coteSiteFeu{pk}')
        new_timeAllumage = request.POST.get(f'timeAllumage{pk}')
        new_longueurEclosion = request.POST.get(f'longueurEclosion{pk}')
        new_xenreg = request.POST.get(f'xenreg{pk}')
        new_yenreg = request.POST.get(f'yenreg{pk}')
        
        #common
        new_name = request.POST.get(f'name{pk}')
        new_region = request.POST.get(f'region{pk}')
        new_ville = request.POST.get(f"ville{pk}")

        #NOTE : update
        simulation.timp = new_timp
        simulation.typeVegetation = new_typeVegetation
        simulation.nbrDepartFeu = new_nbrDepartFeu
        simulation.x1veg = new_x1veg
        simulation.x2veg = new_x2veg
        simulation.y1veg = new_y1veg
        simulation.y2veg = new_y2veg
        simulation.teneurEnEau = new_teneurEnEau
        simulation.hauteurFuelBed = new_hauteurFuelBed
        simulation.emissiviteFuelBed = new_emissiviteFuelBed
        simulation.absorptionFuelBed = new_absorptionFuelBed
        simulation.densiteFuelBed = new_densiteFuelBed
        simulation.diametreFuelBed = new_diametreFuelBed
        simulation.chaleurSpecFeulBed = new_chaleurSpecFeulBed
        simulation.chargeSurface = new_chargeSurface
        simulation.hauteurFlamme = new_hauteurFlamme
        simulation.timeCombustion = new_timeCombustion
        simulation.timeMax = new_timeMax
        simulation.deltat = new_deltat
        simulation.deltax = new_deltax
        simulation.deltay = new_deltay
        simulation.xDebut = new_xDebut
        simulation.xFin = new_xFin
        simulation.yDebut = new_yDebut
        simulation.yFin = new_yFin
        simulation.temperatureAir = new_temperatureAir
        simulation.vitesseDuVent = new_vitesseDuVent
        simulation.directionDuVen = new_directionDuVen
        simulation.pentex = new_pentex
        simulation.pentey = new_pentey
        simulation.temperatureFlamme = new_temperatureFlamme
        simulation.temperatureAllumage = new_temperatureAllumage
        simulation.temperatureBrais = new_temperatureBrais
        simulation.emissiviteBraise = new_emissiviteBraise
        simulation.conductiviteBraise = new_conductiviteBraise
        simulation.conductiviteFlamme = new_conductiviteFlamme
        simulation.viscositeAirChau = new_viscositeAirChau
        simulation.nbEclosion = new_nbEclosion
        simulation.xEclosion = new_xEclosion
        simulation.yEclosion = new_yEclosion
        simulation.coteSiteFeu = new_coteSiteFeu
        simulation.timeAllumage = new_timeAllumage
        simulation.longueurEclosion = new_longueurEclosion
        simulation.xenreg = new_xenreg
        simulation.yenreg = new_yenreg
        simulation.name = new_name
        simulation.region = new_region
        simulation.ville = new_ville

        #TODO: build right drawer
        # simulation.graphic_urls = drawer(float(new_limite_initiale_ox),float(new_limite_initiale_oy), new_simulation_name)

        simulation.save()
        return render(request, 'simulation/simulation_detail.html', {'simulation': simulation})
    
    simulation = get_object_or_404(Simulation, pk=pk)
    return render(request, 'simulation/simulation_edit.html', {'simulation': simulation})


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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
    response = HttpResponse("CSV file saved successfully.", content_type='text/plain')
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
    simulation.is_completed = True
    simulation.save()
    return redirect('view_graphic', pk=pk)


def view_graphic(request, pk):
    simulation = get_object_or_404(Simulation, pk=pk)
    
    if (simulation.is_completed):
        directory_path = f"media/{simulation.name}/images"

        image_paths = []

        for filename in os.listdir(directory_path):
            if filename.endswith(".png"):
                # Check if the file has a .png extension
                image_path = os.path.join(directory_path, filename)
                image_paths.append(image_path)

        urls = sorted(image_paths, key=lambda x: int(x.split('_')[-1].split('.')[0]))

        urls_string = ''
        for i in range(0, len(urls)):
            urls_string += f'{urls[i]}|'

        return render(request, 'simulation/graphic_detail.html', {'simulation': simulation, 'urls': urls_string})
    else:
        return redirect('detail_simulation', pk=pk)
    