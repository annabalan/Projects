class Ingredient():
     def __init__(self, name, quantity, unit):
         self.name = name
         self.quantity = quantity
         self.unit = unit
     def inputline(self, name, quantity, unit):
         self.name = input("Ingredient: ")
         if len(self.name)>0:
             self.quantity = input("Quantity required: ")
             self.unit = input("Unit of measurement: ")
     def combineline(self):
         return self.name + "|" + self.quantity + self.unit

 class Recipe():
     def __init__(self, name, course, servings, cuisine, preptime, cooktime, ttime):
         self.name = name
         self.course = course
         self.servings = servings
         self.cuisine = cuisine
         self.preptime = preptime
         self.cooktime = cooktime
         self.ttime = ttime

class RecipeFile():
    def __init__(self, filenmae, fileIndex):
        self.filename = filename
        self.fileIndex = fileIndex
