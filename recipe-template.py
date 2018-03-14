# templete
def menu():
    ingred = {}
    choice = None
    while choice != "0":
        print(""" Menu
            0 - Exit
            1 - Start Recipe
            2 - View Recipe
            """)

        choice = input("Choice: ")
        print()
        if choice == "0":
            print("Good-bye.")
        elif choice == "1":
            name = input("Recipe Name: ")
            course = input("Course: ")
            cuisne = input("Cuisne: ")
            ptime = input("Prep Time: ")
            time = input("Cook Time: ")
            ttime = input("Total Time: ")
            servings = input("Servings: ")
            #create loop here
            # entry = input("Enter Ingredients: ")
            # instruc = input("List instructions: ")
            # ingred[entry] = instruc
            print(entry, "has been added.")
        elif choice == 2:
            print(name, "/n", course, "/n", cuisine, "/n",  ptime, "/n", time, "/n", ttime, "/n", servings)
        else:
            print("Invalid choice")

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
