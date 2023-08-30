import random
import fruits


def scaler(min,max,value):
    l_scaler = 0
    h_scaler = 1
    scaled = h_scaler - (h_scaler - l_scaler)*(max - value)/(max - min)
    if scaled >= 0 and scaled<= 1:
        return scaled
    else:
        return 0
     
def nutrient_s(n,p,k):
    nitro =(1/3) * n
    phos = (1/3)* p
    potas = (1/3) * k
    a = nitro+phos+potas
    b = 250+250+250
    strenght = a/b
    scaled_strenght = scaler(0,0.3333,strenght)
    return scaled_strenght



def simulate(frui,seas, soilph, water, nutr):
    # dictionary containing plant classes
    plantes = {
        'Tomatoes': fruits.Tomatoes,
        'Corn': fruits.Corn,
    }
    
    # dictionary containing temperature ranges for each season
    seasons = {
        'Winter': [10, 20],
        'Spring': [10, 25],
        'Summer': [21, 32],
        'Fall': [10, 25],
    }
    try:

        season = seasons[seas]
        plant = plantes[frui]
    except:
        season = seasons['Summer']
        plant = plantes['Corn']
    nutrients = nutrient_s(float(nutr[0]), float(nutr[1]), float(nutr[2]))

    # generate random values for temperature, light, and pest
    temperature = random.randrange(season[0], season[1], 1)
    soil_ph = soilph
    soil_water = water
    light = random.randrange(0, 100, 1)/100
    pest = 0
    
    # create plant object and calculate number of fruits produced
    plant = plant(temperature, soil_ph, soil_water, light, nutrients, pest)
    fruits_produced = plant.fruits()
    
    # return number of fruits produced
    return int(fruits_produced)