#Developer: Alan David Portilla Castillo

import requests
import os

def get_commet_data(api_key):
    print("::: COMETS INFORMATION")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        os.system('clear')
        print(f"Comet name: {data['name']} ")
        print(f"Comet Absolute magnitude: {data['absolute_magnitude_h']} ")        
        print(f"Comet Estimated diameter max(KM): {data['estimated_diameter']['kilometers']['estimated_diameter_max']} ")
        print(f"Comet Estimated diameter min(KM): {data['estimated_diameter']['kilometers']['estimated_diameter_min']} ")
        print(f"Comet Estimated diameter max(FT): {data['estimated_diameter']['feet']['estimated_diameter_max']} ")
        print(f"Comet Estimated diameter min(FT): {data['estimated_diameter']['feet']['estimated_diameter_min']} ")
        print(f"last_observation_date: {data['orbital_data']['last_observation_date']} ")
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

api_key_nasa = '5pmYxZELNaKrrxMqAcoCKxVQZf4HgXghzShyO4w2'
get_commet_data(api_key_nasa) 