import requests
from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, 'finder/home.html')


def search(request):
    if request.method == 'POST':
        location = request.POST.get('location', '')
        radius = request.POST.get('radius', 1000)  # Default to 1000 meters

        # Use Google Places API to search for nearby restaurants
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            'location': location,
            'radius': radius,
            'type': 'restaurant',
            'key': settings.GOOGLE_MAPS_API_KEY
        }

        response = requests.get(url, params=params)
        results = response.json().get('results', [])

        context = {
            'results': results,
            'api_key': settings.GOOGLE_MAPS_API_KEY,
            'location': location,
        }
        return render(request, 'finder/results.html', context)

    return render(request, 'finder/home.html')


from django.shortcuts import render

# Create your views here.
