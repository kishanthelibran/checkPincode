from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from geopy.geocoders import Nominatim

# Create your views here.


@api_view(['GET'])
def PinDetails(request):
    pin_code = request.data['pin_code']

    # use nomination api to create a Geo Locator
    geolocator = Nominatim(user_agent="geoapiExercises")

    # find the location
    location = geolocator.geocode(pin_code)

    address = (location.address).split(",")

    # find city and state
    state = address[len(address) - 3]
    city = address[len(address) - 4]

    print(location)
    return JsonResponse({'state': state, 'city': city})
