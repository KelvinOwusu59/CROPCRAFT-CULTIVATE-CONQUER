from functions import scaler as sc


# this is the Crop class
class Crop:
    def __init__(self, temperature, soil_type, water, light, nutrient, pest_parasite):
        self.temperature = temperature
        self.soil_type = soil_type
        self.water = water
        self.light = light
        self.nutrient = nutrient
        self.pest_parasite = pest_parasite

    def leaves(self):
        weight_of_light = 0.8*self.light
        weight_of_nutrients = 0.8*self.nutrient
        weight_of_water = 0.8 * self.water
        weight_of_pest = 0.8*self.pest_parasite
        leaves_produced = (weight_of_water+weight_of_pest+weight_of_light+weight_of_nutrients) / \
            (self.light + self.nutrient + self.water + self.pest_parasite)
        return leaves_produced


# these are the fruits to be produced on the farm
class Tomatoes(Crop):
    # TOTAL_FRUITS_AT_OPTIMUM = 500
    Tempearture_range = [15, 32,]
    SoilPhRange = [6, 7, ]
    MoistureRange = [2.5, 5,]
    MAX_PARASITE = 10
    Max_FLOWER = 100

    def __init__(self, temperature, soil_type, water, light, nutrient, pest_parasite) -> None:
        super().__init__(temperature, soil_type,
                         water, light, nutrient, pest_parasite)
        self.temperature = sc(
            self.Tempearture_range[0], self.Tempearture_range[1], temperature)
        self.water = sc(self.MoistureRange[0], self.MoistureRange[1], water)
        self.nutrient = nutrient
        self.light = light
        self.soil_type = soil_type
        self.pest_parasite = pest_parasite

    def fruits(self):
        temp_weight = 0.40 * self.temperature
        water_weight = 0.10 * self.water
        nutrient_weight = 0.35 * self.nutrient
        light_level = 0.10 * self.light
        soil_ph = 0.06 * self.soil_type
        amount_of_flowers = self.Max_FLOWER*self.leaves()
        plant_growth_factor = temp_weight+water_weight + \
            nutrient_weight+light_level+soil_ph
        # scaled_plant_growth_factor = sc(0,0.64,0,1,plant_growth_factor)
        amount_of_fruits_produced = plant_growth_factor*amount_of_flowers
        print(
            f'plant growth factor{plant_growth_factor} , amoutn of flowers {amount_of_flowers}')
        return amount_of_fruits_produced


class Corn(Crop):
    MAX_PARASITE = 10
    Max_FLOWER = 100
    Tempearture_range = [18, 30]
    SoilPhRange = [6, 7]
    MoistureRange = [2.5, 3]

    def __init__(self, temperature, soil_type, water, light, nutrient, pest_parasite) -> None:
        super().__init__(temperature, soil_type,
                         water, light, nutrient, pest_parasite)
        self.temperature = sc(
            self.Tempearture_range[0], self.Tempearture_range[1], temperature)
        self.water = sc(self.MoistureRange[0], self.MoistureRange[1], water)
        self.nutrient = nutrient
        self.light = light
        self.soil_type = soil_type
        self.pest_parasite = pest_parasite

    def fruits(self):
        temp_weight = 0.218 * self.temperature
        water_weight = 0.28 * self.water
        nutrient_weight = 0.25 * self.nutrient
        light_level = 0.19 * self.light
        soil_ph = 0.06 * self.soil_type
        amount_of_flowers = self.Max_FLOWER*self.leaves()
        plant_growth_factor = temp_weight+water_weight + \
            nutrient_weight+light_level+soil_ph
        amount_of_fruits_produced = plant_growth_factor*amount_of_flowers
        print(self.temperature)
        return amount_of_fruits_produced


