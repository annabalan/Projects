# templete
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
        time = input("Cooke Time: ")
        ttime = input("Total Time: ")
        servings = input("Servings: ")
        #create loop here
            entry = input("Enter Ingredients: ")
            instruc = input("List instructions: ")
            ingred[entry] = instruc
        print(entry, "has been added.")
    elif choice == 2:
        print(name, "/n", ptime, "/n", ttime, "/n", ingred)
    else:
        print("Invalid choice")
