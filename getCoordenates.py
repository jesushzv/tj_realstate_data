# -*- coding: utf-8 -*-
import requests
from stripAccents import strip_accents

#KEY AND BASE URL
API_KEY = 'AIzaSyBgKkGlGYYB6Sa0i2SZEcN36sY0vsdzu8A'
BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

#FUNCTION TO GET AN ADRESS COORDINATES USING GOOGLE MAP'S GEOCODE API
def getCoordenates(address):
    params = {
        'key': API_KEY,
        'address': strip_accents(address)
    }

    response = requests.get(BASE_URL,params=params).json()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']

        return [lat,lon]




