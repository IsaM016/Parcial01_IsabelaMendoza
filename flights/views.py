from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg

def home(request):
    return render(request, 'home.html')


from django.shortcuts import render

# Create your views here

def register_flight(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_flights')
    else:
        form = FlightForm()
    return render(request, 'register_flight.html', {'form': form})

def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'list_flights.html', {'flights': flights})

def flight_statistics(request):
    national_count = Flight.objects.filter(type="Nacional").count()
    international_count = Flight.objects.filter(type="Internacional").count()
    national_avg_price = Flight.objects.filter(type="Nacional").aggregate(Avg('price'))['price__avg'] or 0
    return render(request, 'flight_statistics.html', {
        'national_count': national_count,
        'international_count': international_count,
        'national_avg_price': national_avg_price,
    })