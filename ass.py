#pseudo code

# input=Stories ,.attributes=length,moral lessons,age
# process=create a class stories,pass the attributres,crearte methods story teller and translator.
# output=stories understood or not understood



# 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# input=Story,story_teller,translater,attributes,length,age_group,moral
# process=class story,sub classes to inherit the main class and the methods
# output=story translated 


class Story:
    def __init__(self, length, age_group, moral):
        self.length = length
        self.age_group = age_group
        self.moral = moral


class StoryTeller:
    def __init__(self, name, culture, language):
        self.name = name
        self.culture = culture
        self.language = language

    def tell_story(self, story):
        return Translator.translate(story, self.language)


class Translator:
    
    def translate(story, target_language):
        translated_story = get_translation(story, target_language)
        return translated_story



def get_translation(story, target_language):
    
    
    return "Translated story"


story = Story("2hrs", "40-90 yrs", "how to handle stress")
story_teller = StoryTeller("Mercy", "Maasai", "Maasai")
translator = Translator()

translated_story = story_teller.tell_story(story)
print(translated_story)



# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.
# input=recipe,attributes=name,ingredients,prep_time,cook_method,nutrition
# process=create a class ,create methods,Create another class to inherit the main class which is africanRecipe,and give a method and give instance to run the code
# output=explanation of a recipe on how pizza in Africa is prepared

class Recipe:
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition):
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.cook_method = cook_method
        self.nutrition = nutrition
    
    def __repr__(self):
        return f"The {self.name} in africa is prepared with {', '.join(self.ingredients)} in {self.prep_time} using {self.cook_method}. It has high {self.nutrition}."
        

class AfricanRecipe(Recipe):
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition):
        super().__init__(name, ingredients, prep_time, cook_method, nutrition)
        
    
    def __str__(self):
        return f"{self.name} "


African_chicken_tajine = AfricanRecipe(
    "pizza",
    ["chicken", "onions", "tomatoes",  "lemons", "spices"],
    "30 minutes",
    "Stew",
    "nutritious"
)

print(African_chicken_tajine)
print(repr(African_chicken_tajine))



# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

# input=Species,predators,prey.,attributes=name,diet,lifespan,habitat
# process,create class species and sub classes predator and prey to inherit from the main class 
# output=names,habitat,diet,and lifespan of the animals


class Species:
    def __init__(self, name, diet, lifespan, habitat):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.habitat = habitat

class Predator(Species):
    def __init__(self, name, diet, lifespan, habitat, hunting_style):
        super().__init__(name, diet, lifespan, habitat)
        self.hunting_style = hunting_style
        print(f" the {self.name} is a {self.diet}  and lives for about {self.lifespan} in the {self.habitat} and also {self.hunting_style} prey in bushes.")
        

class Prey(Species):
    def __init__(self, name, diet, lifespan, habitat, speed):
        super().__init__(name, diet, lifespan, habitat)
        
        print(f"{self.name} is a {self.diet} and lives for about {self.lifespan} in the {self.habitat} and run in about {speed} of speed.")

lion = Predator("Lion", "Carnivore", 10, "Savannah", "Ambush")
gazelle = Prey("Gazelle", "Herbivore", 8, "Grasslands", 60)


# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

# input=product,attributes name,price,quantity
# process=create a class product and pass the method to calculate the total value
# output=total value of the products


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

p1 = Product("vegetables", 1.0, 10)
p2 = Product("mango", 2.0, 5)
p3 = Product("cake", 3.0, 3)

total_value = p1.total_value() + p2.total_value() + p3.total_value()
print("Total value of all product=", total_value)



# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
