from unittest import result

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.cache import cache_control


def home(request):
    return render(request, 'finder/home.html')

'''
@login_required(login_url='my-login')
@cache_control(no_cache = True, must_revalidate = True, no_store = True)

'''
def search(request):
    if request.method == 'POST':
        location = '33.7488, -84.3877'

        # Use Google Places API to search for nearby restaurants
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            'location': location,
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


from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Favorite


@login_required(login_url='my-login')
def add_favorite(request):
    if request.method == 'POST':
        restaurant_name = request.POST.get('restaurant_name')
        rating = request.POST.get('rating')
        distance = request.POST.get('distance')
        address = request.POST.get('address')

        # Ensure the restaurant is not already in the user's favorites
        if not Favorite.objects.filter(user=request.user, restaurant_name=restaurant_name).exists():
            Favorite.objects.create(
                user=request.user,
                restaurant_name=restaurant_name,
                rating=rating,
                distance=distance,
                address=address
            )
            return JsonResponse({'status': 'success', 'message': 'Added to favorites'})

        return JsonResponse({'status': 'error', 'message': 'Restaurant already in favorites'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@login_required(login_url='my-login')
def dashboard(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'finder/dashboard.html', {'favorites': favorites})


from django.shortcuts import render

# Create your views here.
