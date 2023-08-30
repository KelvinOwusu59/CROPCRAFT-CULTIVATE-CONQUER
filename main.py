import random
import fruits
from functions import nutrient_s as nt


def console():
    # this is a console version of the game just for illustrative purposes
    fruitsAvailable = {
        'Tomatoes': fruits.Tomatoes,
        'Corn': fruits.Corn,
    }
    seasons = {
        'winter': [10, 20],
        'spring': [10, 25],
        'summer': [21, 32],
        'fall': [10, 25],
    }
    print('PLease select the type of crops you will like to grow Also select the seasons ')
    print(
        f'these are the crops available {fruitsAvailable.keys()} seperate with a coma if you want to grow more than one type of crop')
    crops = input('select crop/s')
    crop = fruitsAvailable[crops.strip()]
    print(f'these are the seasons available {seasons.keys()} ')
    seas = input('select season')
    season = seasons[seas.strip()]
    print('now that you have selected the crop you want to grow \n it is time to select the fertilizers you intend to use to promote healthy growth of your crops')
    print(f'Select your fertilizers it should be in this format (Nitrogen, phoseporous,Potassium) each fertilizer should be a positive interger between 0 and 250 your final input should be like this 250,250,250')
    print()
    fert = input('input nutrient proporion').split(',')
    nutrients = nt(float(fert[0]), float(fert[1]), float(fert[2]))
    print('these are your selections {} ,{}, {}'.format(crop, season, nutrients), )
    print()
    print('initializing preambles')
    days = 30
    for day in range(days):
        print(f'for day {day} setting up variables')
        temperature = random.randrange(season[0], season[1], 1)
        soil_ph = 6.7
        soil_water = 2.5
        soil_nutrient = nutrients
        light = random.randrange(0, 100, 1)/100
        print(light, temperature)
        pest = 0
        plant = crop(temperature, soil_ph, soil_water, light, nutrients, pest)
        fruits_produced = plant.fruits()
        print('fruits produced today {}'.format(fruits_produced))
    # while True:

    #     pass
    pass


def simulate(fruit, season, soilph, water, nutr, timer):
    plantes = {
        'Tomatoes': fruits.Tomatoes,
        'Corn': fruits.Corn,
    }
    plant = plantes[fruit]
    nutrients = nt(float(nutr[0]), float(nutr[1]), float(nutr[2]))

    temperature = random.randrange(season[0], season[1], 1)
    soil_ph = soilph
    soil_water = water
    light = random.randrange(0, 100, 1)/100
    print(light, temperature)
    pest = 0
    plant = plant(temperature, soil_ph, soil_water, light, nutrients, pest)
    fruits_produced = plant.fruits()
    print('fruits produced today {}'.format(fruits_produced))
    return fruits_produced



if __name__ == "__main__":
    # Your code goes here
    console()
