from main.models import Viaje
from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from main.auth import User


@login_required
def home(request):
    viajes = Viaje.objects.all() 

    context = {
        'viajes': viajes
    }
    return render(request, 'index.html', context)


@login_required
def create(request):
    if request.method == "GET":
        return render(request,"create.html")

    if request.method == "POST":
        destination = request.POST['destination']
        travel_star = request.POST['star']
        travel_end = request.POST['end']
        plan = request.POST['plan']
        user_id = int(request.session['user']['id'])
        new_plan = Viaje.objects.create(
            destination = destination, travel_star = travel_star, travel_end = travel_end,
            plan=plan, owner_user_id = user_id)
    return redirect("/")

@login_required
def view(request, id):
    pass

