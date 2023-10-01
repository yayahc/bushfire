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

@login_required
def simulations(request):
    if request.method == 'POST':
        simulation_name = request.POST.get("new-simulation")
        simulation = Simulation.objects.create(name=simulation_name, user=request.user)
        return redirect("simulations")

    simulations = Simulation.objects.filter(user=request.user, is_completed=False).order_by("-id")

    # pagination 4 items per page
    paginator = Paginator(simulations, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"simulations": simulations, "page_obj": page_obj}

    # NOTE: Need to change the html file to crud.html for displaying the todo's
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
        simulation.name = new_name
        simulation.save()
        return render(request, 'simulation/simulation_detail.html', {'simulation': simulation})
    
    simulation = get_object_or_404(Simulation, pk=pk)
    return render(request, 'simulation/simulation_edit.html', {'simulation': simulation})


def complete_simulation(request, pk):
    todo = get_object_or_404(Simulation, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
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
        content += f"User: {simulation.user}\n\n\n"
        content += "--------------------------------------\n\n\n"

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="all_simulations.txt"'
    return response


@login_required
def upload_simulation(request):
    if request.method == 'POST':
        form = UploadSimulationForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            txt_file = form.cleaned_data['txt_file']
            content = txt_file.read().decode('utf-8')

            # Use regular expressions to extract information from the content
            created_on_match = re.search(r'Created On: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
            updated_on_match = re.search(r'Updated On: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', content)
            user_match = re.search(r'User: (\w+)', content)

            if created_on_match and updated_on_match and user_match:
                created_on = created_on_match.group(1)
                updated_on = updated_on_match.group(1)
                user = user_match.group(1)

                # Create a new Simulation instance with the extracted data
                simulation = Simulation.objects.create(
                    name=name,
                    created_on=created_on,
                    updated_on=updated_on,
                    user=request.user,  # Set the user who uploaded the file
                )

                # Optionally, you can redirect to a success page or display a message
                return redirect('simulations')

    else:
        form = UploadSimulationForm()

    return render(request, 'simulation/upload_simulation.html', {'form': form})
