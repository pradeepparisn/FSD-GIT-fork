from django.shortcuts import render, redirect
from .models import Journey, Car, Route, Utility
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['nickname', 'make', 'model', 'year', 'fuel_type', 'drive', 'transmission', 'v_class', 'disp', 'city_km_per_gallon', 'highway_km_per_gallon', 'icon_id']

def home(request):
    return render(request, 'carbontracker/home.html')

def journey_list(request):
    journeys = Journey.objects.all()
    return render(request, 'carbontracker/journey_list.html', {'journeys': journeys})

class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = ['route', 'car', 'journey_date', 'trans_mode', 'route_save']

def journey_add(request):
    if request.method == 'POST':
        form = JourneyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journey_list')
    else:
        form = JourneyForm()
    return render(request, 'carbontracker/journey_add.html', {'form': form})

def vehicle_list(request):
    vehicles = Car.objects.all()
    return render(request, 'carbontracker/vehicle_list.html', {'vehicles': vehicles})

def vehicle_add(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = CarForm()
    return render(request, 'carbontracker/vehicle_add.html', {'form': form})

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'city_distance', 'highway_distance']

def route_list(request):
    routes = Route.objects.all()
    return render(request, 'carbontracker/route_list.html', {'routes': routes})

def route_add(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm()
    return render(request, 'carbontracker/route_add.html', {'form': form})

def utility_list(request):
    utilities = Utility.objects.all()
    return render(request, 'carbontracker/utility_list.html', {'utilities': utilities})

def utility_add(request):
    # Placeholder for adding utility logic
    return render(request, 'carbontracker/utility_add.html')
