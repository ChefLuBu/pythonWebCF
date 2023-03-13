class Recipe(object):
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int()
        self.difficulty = ""

    def get_name(self):
        output = "Recipe: " + self.name 
        return output
    
    def set_name(self, name):
        self.name = name
        
    def get_cooking_time(self):
        output = "Cooking time: " + str(self.cooking_time) + " minutes"
        return output
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = int(cooking_time)
   
    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def get_ingredients(self):
        print('\nIngredients:')
        for ingredient in self.ingredients:
            print(' - ' + ingredient)
        # for ingredient in self.ingredients:
        #     print(' - ' + str(self.ingredient))

    def search_ingredient(self, ingredient, ingredients):
        if(ingredient in ingredients):
            return True
        else:
            return False

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def recipe_search(self, recipes_list, ingredient):
        data = recipes_list
        search_term = ingredient
        for recipe in data:
            if search_term in recipe.ingredients:
                print(recipe.name)
            # if self.search_ingredient(search_term, recipe.ingredients):
            #     print(recipe.name)
    
    def calc_difficulty(self, cooking_time, ingredients):
            if (cooking_time) < 10 and len(ingredients) < 4:
                difficulty = "easy"
            elif (cooking_time) < 10 and len(ingredients) <= 4:
                difficulty = "medium"
            elif (cooking_time) >= 10 and len(ingredients) < 4:
                difficulty = "intermediate"
            elif (cooking_time) >= 10 and len(ingredients) >= 4:
                difficulty = "hard"
                return difficulty
            else:
                print("No difficulty found")
            return difficulty
    
    
    def get_difficulty(self):
        difficulty = self.calc_difficulty(self.cooking_time, self.ingredients)
        output = "Difficulty: " + str(self.cooking_time) + " minutes"
        self.difficulty= difficulty
        return output

    def __str__(self):
        output = '\nRecipe: ' + self.name + '\n'
        'Cooking time: ' + str(self.cooking_time) + ' minutes' + '\n'
        'Difficulty: ' + self.difficulty + '\n'
        '\nIngredients:\n'
        for ingredient in self.ingredients:
            output += ingredient + '\n'
        return output
    
    def view_recipe(self):
        print('\nRecipe: ' + self.name + '\n')
        print('Cooking time: ' + str(self.cooking_time) + ' minutes')
        self.get_ingredients()


recipes_list = []

tea= Recipe("tea")
tea.add_ingredients("Water", "Tea leaves", "Sugar")
tea.set_cooking_time(5)
tea.get_difficulty()

recipes_list.append(tea)

coffee = Recipe("coffee")
coffee.add_ingredients("Water", "Coffee beans", "Sugar")
coffee.set_cooking_time(5)
coffee.get_difficulty()

recipes_list.append(coffee)

cake = Recipe("cake")
cake.add_ingredients("Flour", "Sugar", "Eggs", "Milk", "Butter", "Vanilla Essence", "Baking Poweder")
cake.set_cooking_time(50)
cake.get_difficulty()

recipes_list.append(cake)

banana_smoothie = Recipe("banana smoothie")
banana_smoothie.add_ingredients("Banana", "Milk", "Sugar", "Peanut Butter", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()

recipes_list.append(banana_smoothie)


print('Recipes List:    ')
for recipe in recipes_list:
    print(recipe)

print('Recipes with Sugar:    ')
tea.recipe_search(recipes_list, "Sugar")

print('Recipes with Water:    ')
tea.recipe_search(recipes_list, "Water")

print('Recipes with Bananas:    ')
tea.recipe_search(recipes_list, "Bananas")