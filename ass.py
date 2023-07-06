
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
    def __init__(self, title, length, moral_lesson, age_group):
        self.title = title
        self.length_of_story = length
        self.moral_lesson = moral_lesson
        self.age_group = age_group

    def display_story(self):
        return f"{self.title}"


class StoryTeller(Story):
    def __init__(self, story_type, language, title, length, moral_lesson, age_group):
        super().__init__(title, length, moral_lesson, age_group)
        self.story_type = story_type
        self.language = language
        self.stories = []

    def narrate_story(self):
        return f"{self.story_type} is being narrated in {self.language}"

    def add_story(self, story):
        self.stories.append(story)

class Translator(Story):
    def __init__(self, translated_language):
        super().__init__("title", "length", "moral_lesson", "age_group")
        self.translated_language = translated_language

    def translate_story(self):
        print(f"Te story is translated into {self.translated_language}.")


story = Story("Born a crime", 400, "Hardwork", 15)

print(story.display_story())

teller = StoryTeller("Novel", "English", story.title, story.length_of_story, story.moral_lesson, story.age_group)
print(teller.narrate_story())
teller.add_story(story)
translator = Translator("Lapvona")
translator.translate_story()



# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.
# input=recipe,attributes=name,ingredients,prep_time,cook_method,nutrition
# process=create a class ,create methods,Create another class to inherit the main class which is africanRecipe,Ethiopian recipe and Nigerian recipe give a method and give instance to run the code
# output=Display the preparation process for each recipe and the recipe details for each recipe.


# class Recipe:
#     def __init__(self, name,ingredients,country, prep_time, cook_method, nutrition):
#         self.name = name
#         self.ingredients=ingredients
#         self.country=country
#         self.prep_time = prep_time
#         self.cook_method = cook_method
#         self.nutrition = nutrition
    
#     def display_recipe(self):
#         return f"{self.name},{self.ingredients},{self.country},{self.prep_time},{self.cook_method},{self.nutrition}"
# class AfricanRecipe(Recipe):
#     def __init__(self, name,country,ingredients ):
#         super().__init__("name","country","ingredients", "prep_time", "cook__method", "nutrition")
        
    
#     def prepare(self):
#         return f"The {self.name} recipe in Africa is being prepared."

# class EthiopianRecipe(Recipe):
#     def __init__(self):
#         super().__init__("name," "prep_time", "cook_method", "nutrition")
    
#     def prepare(self):
#         return f"The {self.name} recipe in Ethiopia is being prepared."

# class NigerianRecipe(Recipe):
#     def __init__(self, name, prep_time, cook_method, nutrition):
#         super().__init__(name, prep_time, cook_method, nutrition)
    
#     def prepare(self):
#         return f"The {self.name} recipe in Nigeria is being prepared."


# African_pizza = AfricanRecipe( "pizza", "30 minutes", "frying","nutritious")
# print(African_pizza.prepare())
# print(African_pizza.display_recipe())

# Ethiopian_rice = EthiopianRecipe("ricre","2 hours","boiling","healthy")
# print(Ethiopian_rice.prepare())
# print(Ethiopian_rice.display_recipe())

# Nigerian_pilau = NigerianRecipe( "pilau","45 minutes","One-pot","delicious")
# print(Nigerian_pilau.prepare())
# print(Nigerian_pilau.display_recipe())


# class Recipe:
#     def __init__(self, name, ingredients, country, prep_time, cook_method, nutrition):
#         self.name = name
#         self.ingredients = ingredients
#         self.country = country
#         self.prep_time = prep_time
#         self.cook_method = cook_method
#         self.nutrition = nutrition
    
#     def display_recipe(self):
#         return f"{self.name}, {self.ingredients}, {self.country}, {self.prep_time}, {self.cook_method}, {self.nutrition}"





class Recipe:
    def __init__(self, name, ingredients, country, prep_time, cook_method, nutrition):
        self.name = name
        self.ingredients = ingredients
        self.country = country
        self.prep_time = prep_time
        self.cook_method = cook_method
        self.nutrition = nutrition
    
    def display_recipe(self):
        return f"{self.name}, {self.ingredients}, {self.country}, {self.prep_time}, {self.cook_method}, {self.nutrition}"


class AfricanRecipe(Recipe):
    def __init__(self, name, country, ingredients, prep_time, cook_method, nutrition):
        super().__init__(name, ingredients, country, prep_time, cook_method, nutrition)
        
    def prepare(self):
        return f"The {self.name} is a food prepared in {self.country} ."


class EthiopianRecipe(Recipe):
    def __init__(self, name, prep_time, cook_method, nutrition):
        super().__init__(name, "ingredients", "Ethiopia", prep_time, cook_method, nutrition)
    
    def prepare(self):
        return f"The {self.name} food prepared in {self.country} ."


class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition):
        super().__init__(name, ingredients, "Nigeria", prep_time, cook_method, nutrition)
    
    def prepare(self):
        return f"The {self.name} is food prepared in {self.country} ."


African_pizza = AfricanRecipe("pizza", "Africa", "ingredients", "30 minutes", "cook_method", "nutrition")
print(African_pizza.prepare())
print(African_pizza.display_recipe())

Ethiopian_rice = EthiopianRecipe("rice", "2 hours", "boiling", "healthy")
print(Ethiopian_rice.prepare())
print(Ethiopian_rice.display_recipe())

Nigerian_pilau = NigerianRecipe("pilau", "rice", "45 minutes", "One-pot", "delicious")
print(Nigerian_pilau.prepare())
print(Nigerian_pilau.display_recipe())




# # **Wildlife Preservation:** You're a wildlife conservationist working on a
# # program to track different species in a national park. Each species has its own
# # characteristics and behaviors, such as its diet, typical lifespan, migration
# # patterns, etc. Some species might be predators, others prey. You'll need to

# # create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# # these classes might relate to each other through inheritance.

# # input=Species,predators,prey.,attributes=name,diet,lifespan,habitat
# # process,create class species and sub classes predator and prey to inherit from the main class 
# # output=names,habitat,diet,and lifespan of the animals


# class Species:
#     def __init__(self, name, diet, lifespan, habitat, migration_pattern):
#         self.name = name
#         self.diet = diet
#         self.lifespan = lifespan
#         self.habitat = habitat
#         self.migration_pattern = migration_pattern

# class Predator(Species):
#     def __init__(self, name, diet, lifespan, habitat, hunting_style, migration_pattern):
#         super().__init__(name, diet, lifespan, habitat, migration_pattern)
#         self.hunting_style = hunting_style
#         print(f"The {self.name} is a {self.diet} and lives for about {self.lifespan} in the {self.habitat} and also {self.hunting_style} prey in bushes and is migrating from {self.migration_pattern}.")

# class Prey(Species):
#     def __init__(self, name, diet, lifespan, habitat, migration_pattern, speed):
#         super().__init__(name, diet, lifespan, habitat, migration_pattern)
#         self.speed = speed
#         print(f"{self.name} is a {self.diet} and lives for about {self.lifespan} in the {self.habitat} and migrating from {self.migration_pattern}, running at a speed of {self.speed}.")

# lion = Predator("Lion", "Carnivore", 10, "Savannah", "Ambush", "bushes to bushes ")
# gazelle = Prey("Gazelle", "Herbivore", 8, "Grasslands", "grasslands to grasslands", 60)

class Species:
    def __init__(self, name, diet, lifespan, habitat, migration_pattern):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.habitat = habitat
        self.migration_pattern = migration_pattern

    def display_information(self):
        print(f"{self.name},{self.diet},{self.lifespan},{self.habitat},{self.migration_pattern}")
        
class Predator(Species):
    def __init__(self, name, diet, lifespan, habitat, hunting_style, migration_pattern):
        super().__init__(name, diet, lifespan, habitat, migration_pattern)
        self.hunting_style = hunting_style

    def display_information(self):
        super().display_information()
        print(f"Hunting style :{self.hunting_style}")


class Prey(Species):
    def __init__(self, name, diet, lifespan, habitat, migration_pattern, speed):
        super().__init__(name, diet, lifespan, habitat, migration_pattern)
        self.speed = speed

    def display_information(self):
        super().display_information()
        print(f"Speed: {self.speed}")


lion = Predator("Lion", "Carnivore", 10, "Savannah", "Ambush", "bushes to bushes")
lion.display_information()
gazelle = Prey("Gazelle", "Herbivore", 8, "Grasslands", "grasslands to grasslands", 60)
gazelle.display_information()




# 4. **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.
class Artist:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def perform(self):
        return f"{self.name} from {self.country} is performing singing gospel"


class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time


class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.performances = []

    def add_performance(self, performance):
        self.performances.append(performance)

    def get_schedule(self):
        sorted_performances = sorted(self.performances, key=lambda p: p.start_time)
        schedule = ""
        for performance in sorted_performances:
            schedule += f"{performance.start_time} - {performance.end_time}: {performance.artist.perform()}"
        return schedule


class ConcertStage(Stage):
    def __init__(self, name, capacity, sound_system):
        super().__init__(name, capacity)
        self.sound_system = sound_system


class AcousticStage(Stage):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)


artist1 = Artist("Artist 1", "Country 1")
artist2 = Artist("Artist 2", "Country 2")
performance1 = Performance(artist1, "10:00", "11:00")
performance2 = Performance(artist2, "12:00", "13:00")

concert_stage = ConcertStage("Main Stage", 1000, "High-end Sound System")
acoustic_stage = AcousticStage("Acoustic Stage", 500)

concert_stage.add_performance(performance1)
acoustic_stage.add_performance(performance2)

print(concert_stage.get_schedule())
print(acoustic_stage.get_schedule())





# # Create a class called Product with attributes for name, price, and quantity.
# # Implement a method to calculate the total value of the product (price * quantity).
# # Create multiple objects of the Product class and calculate their total values.

# # input=product,attributes name,price,quantity
# # process=create a class product and pass the method to calculate the total value
# # output=total value of the products


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

p1 = Product("vegetables", 4.0, 10)
p2 = Product("mango", 2.0, 5)
p3 = Product("cake", 9.0, 3)

total_value = p1.total_value() + p2.total_value() + p3.total_value()
print( total_value)

# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
#input=Class student,atrributes name,age,grades,add methods display_student_info,average_grade,has_passed
#process=create base class Student,pass the attributes,name,age and grades.create methodsdisplay students info,average and has_passed
#output=name,age and average grade 

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_student_info(self):
        print(f"{self.name} is {self.age} years old and she scored {self.grades}")

    def average_grade(self):
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade

    def has_passed(self):
        average_grade = self.average_grade()
        if average_grade >= 60:
            return True
        else:
            return False


student = Student("Mercy", 18, [80, 70, 90, 65])

student.display_student_info()

average_grade = student.average_grade()
print("Average Grade is", average_grade)

has_passed = student.has_passed()
print("Passed:", has_passed)


# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_book_info(self):
        print(f" {self.title}:{self.author}:{self.copies}")
        
class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        return found_books

    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        return found_books

    def display_book_details(self, book):
        book.display_book_info()


# Example usage
library = LibraryCatalog()

# Add books
book1 = Book("Python Programming", "John Smith", 5)
book2 = Book("Introduction to Java", "Jane Doe", 3)
book3 = Book("Data Structures and Algorithms", "Alice Johnson", 2)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search by title
found_books = library.search_by_title("python programming")
if found_books:
    print(f"Found {len(found_books)} book(s) by title:")
    for book in found_books:
        library.display_book_details(book)
else:
    print("No books found by title.")

# Search by author
found_books = library.search_by_author("Jane Doe")
if found_books:
    print(f"Found {len(found_books)} book(s) by author:")
    for book in found_books:
        library.display_book_details(book)
else:
    print("No books found by author.")
