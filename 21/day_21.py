import time
import os


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}"
              .format(time.time()-t) + ' sec')
        return ret
    return wrapper_method


class DayTwentyOne():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_21.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = contents

    @profiler
    def part_one(self):

        total_ingredients = set()
        total_allergens = set()
        all_foods = []
        result = 0

        for line in self.lines:
            line = line.strip().strip(")")
            ingredients, allergens = line.split(" (contains ")
            ingredientsSet = set(ingredients.split())
            allergensSet = set(allergens.split(", "))
            total_ingredients.update(ingredientsSet)
            total_allergens.update(allergensSet)

            all_foods.append(
                {
                    "ingredients": ingredientsSet.copy(),
                    "allergens": allergensSet.copy()
                }
            )

        notAllergens = total_ingredients.copy()

        for allergen in total_allergens:
            possibleIngredients = total_ingredients.copy()
            for food in all_foods:
                if allergen in food["allergens"]:
                    possibleIngredients.intersection_update(food["ingredients"])
            notAllergens.difference_update(possibleIngredients)

        for food in all_foods:
            result += len(
                notAllergens & food["ingredients"]
            )

        return result

    def part_two(self):
        total_ingredients = set()
        total_allergens = set()
        all_foods = []
        result = 0

        for line in self.lines:
            line = line.strip().strip(")")
            ingredients, allergens = line.split(" (contains ")
            ingredientsSet = set(ingredients.split())
            allergensSet = set(allergens.split(", "))
            total_ingredients.update(ingredientsSet)
            total_allergens.update(allergensSet)

            all_foods.append(
                {
                    "ingredients": ingredientsSet.copy(),
                    "allergens": allergensSet.copy()
                }
            )

        allergen_list = {}

        for allergen in total_allergens:
            allergen_list[allergen] = total_ingredients.copy()
            for food in all_foods:
                if allergen in food["allergens"]:
                    allergen_list[allergen].intersection_update(food["ingredients"])

        ingredientsFound = {}
        while len(ingredientsFound) < len(allergen_list):
            for allergen in allergen_list:
                if allergen not in ingredientsFound and len(allergen_list[allergen]) == 1:
                    for otherAllergen in allergen_list:
                        if otherAllergen != allergen:
                            allergen_list[otherAllergen] -= allergen_list[allergen]
                    ingredientsFound[allergen] = list(allergen_list[allergen])[0]

        allergNames = list(ingredientsFound.keys())
        allergNames.sort()
        allergGibberish = []

        for name in allergNames:
            allergGibberish.append(ingredientsFound[name])

        result = ",".join(allergGibberish)
        return result


day_twentyone = DayTwentyOne()
print("How many times do any of those ingredients appear?")
print(day_twentyone.part_one())
print("=========================================")
print("What is your canonical dangerous ingredient list?")
print(day_twentyone.part_two())
