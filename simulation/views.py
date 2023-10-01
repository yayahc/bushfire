from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import UserRegistrationForm, SimulationForm
from .models import Simulation

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
    """
    Updating todo as completed item

    Args:
        pk (Integer): Todo ID - primary key
    """    
    todo = get_object_or_404(Simulation, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_simulation(request, pk):    
    simulation = get_object_or_404(Simulation, id=pk, user=request.user)
    simulation.delete()
    return redirect("simulations")
