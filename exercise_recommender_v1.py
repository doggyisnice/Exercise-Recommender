import sqlite3



def greet():
    print("Welcome to the Exercise Recommender")
    print("Please select an option from the menu below")
    print("1. Search for an exercise")
    print("2. Add an exercise")
    print("3. Delete an exercise")
    print("4. Exit")

def muscle_group():
    print( "Please enter the muscle group you would like to search (Chest, Back, Shoulders, Arms, Legs, abdominals))")
    muscle_group = "%" + input("Muscle Group: ") + "%"
    print(f"Searching for {muscle_group} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE muscle_group LIKE ?', (muscle_group,))
    for item in c.fetchall():
        print(item)
        print("--------------------------")
    connection.commit()
    connection.close()


def exercise():
    print("Please enter the exercise you would like to search")
    exercise = "%" + input("Exercise: ") + "%"
    print(f"Searching for {exercise} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE exercise LIKE ?', (exercise,))
    for item in c.fetchall():
        print(item)
        print("--------------------------")
    connection.commit()
    connection.close()  

def level():
    print("Please enter the level you would like to search (beginner, intermediate, advanced)")
    level = "%" + input("Level: ") + "%"
    print(f"Searching for {level} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE level LIKE ?', (level,))
    for item in c.fetchall():
        print(item)
        print("--------------------------")
    connection.commit()
    connection.close()

        


def u_l_c():
    print("Please enter the Upper/Lower/Compound you would like to search")
    u_l_c = "%" + input("Upper/Lower/Compound: ") + "%"
    print(f"Searching for {u_l_c} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE u_l_c LIKE ?', (u_l_c,))
    for item in c.fetchall():
      print(item)
      print("--------------------------")
    connection.commit()
    connection.close()
    

def p_p():
    print("Please enter the Push/Pull you would like to search")
    p_p = "%" + input("Push/Pull: ") + "%"
    print(f"Searching for {p_p} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE p_p LIKE ?', (p_p,))
    for item in c.fetchall():
      print(item)
      print("--------------------------")
    connection.commit()
    connection.close()

def modality():
    print("Please enter the modality you would like to search")
    modality = "%" + input("Modality: FW/C") + "%"
    print(f"Searching for {modality} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE modality LIKE ?', (modality,))
    list = c.fetchall()
    print(c.fetchall())
    connection.commit()
    connection.close()

def joint():
    print("Please enter the joint you would like to search")
    joint = "%" + input("Joint: ") + "%"
    print(f"Searching for {joint} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT exercise FROM exercise WHERE joint LIKE ?', (joint,))
    print(c.fetchall())
    connection.commit()
    connection.close()

    

def search():

    search_options()
    option = input("Option: ")
    if option == "1":
        muscle_group()
    elif option == "2":
        exercise()
    elif option == "3":
        level()
    elif option == "4":
        u_l_c()
    elif option == "5":
        p_p()
    # elif option == "6":
    #     modality()
    # elif option == "7":
    #     joint()
    elif option == "6":
        exit()
    else:
        print("Invalid option")
        search()         
    option = input("Option: ")   
    if option == "1":
        search()
    elif option == "2":
        exit()
    
    
    

def add():
    print("Please enter the muscle group you would like to add")
    muscle_group = input("Muscle Group: ")
    print(f"Adding {muscle_group} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('INSERT INTO exercise VALUES (?,?,?,?,?,?,?,?)', row.split(","))
    print(c.fetchall())
    connection.commit()
    connection.close()

def delete():
    print("Please enter the muscle group you would like to delete")
    muscle_group = input("Muscle Group: ")
    print(f"Deleting {muscle_group} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('DELETE FROM exercise WHERE muscle_group LIKE ?', (muscle_group))
    print(c.fetchall())
    connection.commit()
    connection.close()

def exit():
    print("Thank you for using the Exercise Recommender")
    print("Goodbye")

def search_options():
    print("What would you like to search by?")
    print("1. Muscle Group")
    print("2. Exercise")
    print("3. Level")
    print("4. Upper/Lower/Compound")
    print("5. Push/Pull")
    # print("6. Modality")
    # print("7. Joint")
    print("6. Exit")




def program():
    greet()
    option = input("Option: ")
    if option == "1":
        search()
    elif option == "2":
        add()
    elif option == "3":
        delete()
    elif option == "4":
        exit()
    else:
        print("Invalid option")
        program()

program()

