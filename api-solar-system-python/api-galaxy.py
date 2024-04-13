import requests
import os

def diplay():
    print("### Main menu####")
    print("[1]. Planets")
    print("[2]. Moons")
    print("[3]. Stars")
    print("[4]. Asteroid")
    print("[5]. Comets")
    print("[6]. Exit")
    opt = input("::: Press any options:::")
    return opt

def evaluate(option, info):
    if (option == '1'):
        planets = list(filter(lambda x: x['bodyType'] == "Planet", info['bodies']))
        
        for planet in planets:
            print("Nombre: "  + planet['englishName'] + "  Gravedad: " + str(planet['gravity']) + "  Inclinacion: " + str(planet['inclination']) + "  Es un planeta?: " + str(planet['isPlanet']))
    if (option == '2'):
        moons = list(filter(lambda x: x['bodyType'] == "Moon", info['bodies']))
        
        for moon in moons:
            print("Nombre: "  + moon['englishName'] + "  Gravedad: " + str(moon['gravity']) + "  Inclinacion: " + str(moon['inclination']) + "  Es un planeta?: " + str(moon['isPlanet']))
    if (option == '3'):
        stars = list(filter(lambda x: x['bodyType'] == "Star", info['bodies']))
        
        for star in stars:
            print("Nombre: "  + star['englishName'] + "  Gravedad: " + str(star['gravity']) + "  Inclinacion: " + str(star['inclination']) + "  Es un planeta?: " + str(star['isPlanet']))
    if (option == '4'):
        asteroids = list(filter(lambda x: x['bodyType'] == "Asteroid", info['bodies']))
        
        for asteroid in asteroids:
            print("Nombre: "  + asteroid['englishName'] + "  Gravedad: " + str(asteroid['gravity']) + "  Inclinacion: " + str(asteroid['inclination']) + "  Es un planeta?: " + str(asteroid['isPlanet']))
    if (option == '5'):
        comets = list(filter(lambda x: x['bodyType'] == "Comet", info['bodies']))
        
        for comet in comets:
            print("Nombre: "  + comet['englishName'] + "  Gravedad: " + str(comet['gravity']) + "  Inclinacion: " + str(comet['inclination']) + "  Es un planeta?: " + str(comet['isPlanet']))

def get_data():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error {e}")

os.system("clear")
print(":::Solar System Information:::")
info = get_data()
option = diplay()

while option != '6':
    evaluate(option, info)
    option = diplay()