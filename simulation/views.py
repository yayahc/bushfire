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
import matplotlib.pyplot as plt

def drawer(x,y, title):
    plt.scatter(x, y)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title(f'Coordinate Graphic for Simulation {title}')
    plt.grid(True)

    # Save the plot to a file
    temp_file = os.path.join('media', f'simulation_{title}_graphic.png')
    plt.savefig(temp_file)
    plt.close()
    return f'simulation_{title}_graphic.png'


@login_required
def simulations(request):
    if request.method == 'POST':
        simulation_name = request.POST.get("new-simulation")
        simulation_x = request.POST.get("new-simulation-x")
        simulation_y = request.POST.get("new-simulation-y")
        simulation_graphic = drawer(simulation_x,simulation_y, simulation_name)
        simulation = Simulation.objects.create(name=simulation_name, x=simulation_x, y=simulation_y, user=request.user, graphic=simulation_graphic)
        return redirect("simulations")

    simulations = Simulation.objects.order_by("-id")

    # pagination 4 items per page
    paginator = Paginator(simulations, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"simulations": simulations, "page_obj": page_obj}
    return render(request, "simulation/simulations.html", context)


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
    

def update_simulation(request, pk):
    simulation = get_object_or_404(Simulation, id=pk, user=request.user)
    if request.method == 'POST':

        new_name = request.POST.get(f"simulation_{pk}")
        new_x = request.POST.get(f"simulation_x_{pk}")
        new_y = request.POST.get(f"simulation_y_{pk}")

        simulation.name = new_name
        simulation.x = new_x
        simulation.y = new_y

        simulation.save()
        return render(request, 'simulation/simulation_detail.html', {'simulation': simulation})
    
    simulation = get_object_or_404(Simulation, pk=pk)
    return render(request, 'simulation/simulation_edit.html', {'simulation': simulation})


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

    content = f"Simulation Name: {simulation.name}\n"
    content += f"Created On: {simulation.created_on}\n"
    content += f"Updated On: {simulation.updated_on}\n"
    content += f"User: {simulation.user}\n"

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{simulation.name}.txt"'
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
    return render(request, 'simulation/graphic_detail.html', {'simulation': simulation})
