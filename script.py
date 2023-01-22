import sqlite3

narrow = ""
exercise_list = []
search_count = 0

def greet():
    print("Welcome to the Exercise Recommender")
    print("Please select an option from the menu below")
    print("1. Search for an exercise")
    print("2. Add an exercise")
    print("3. Delete an exercise")
    print("4. Exit")

def muscle_group():
    print("Please enter the muscle group you would like to search")
    muscle_group = "%" + input("Muscle Group: ") + "%"
    print("would you like to narrow down your search more?")
    print("1. Yes")
    print("2. No")
    choice = input("Choice: ")
    if choice == "1":
        filter_by()
    print(f"Searching for {muscle_group} exercises")
    global exercise_list
    if search_count == 0:
      connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
      c = connection.cursor()
    #   c.execute('SELECT exercise FROM exercise WHERE muscle_group LIKE ?', (muscle_group,))
      c.execute('SELECT exercise FROM exercise WHERE muscle_group LIKE ? AND level LIKE ?', (muscle_group, level))
      print(c.fetchall())
      c.execute('SELECT * FROM exercise WHERE muscle_group LIKE ?', (muscle_group,))
      exercise_list = (c.fetchall())
      connection.commit()
      connection.close()
    else:
      connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
      c = connection.cursor()
      c.execute('SELECT exercise FROM exercise WHERE muscle_group LIKE ? AND level LIKE ?', (muscle_group, level))
      print(c.fetchall())

def exercise():
    print("Please enter the exercise you would like to search")
    exercise = "%" + input("Exercise: ") + "%"
    print(f"Searching for {exercise} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT * FROM exercise WHERE exercise LIKE ?', (exercise,))
    print(c.fetchall())
    connection.commit()
    connection.close()  

def level():
    print("Please enter the level you would like to search")
    level = "%" + input("Level: ") + "%"
    narrow = level
    print(f"Searching for {level} exercises")
    global exercise_list
    if search_count == 0:
      connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
      c = connection.cursor()
      c.execute('SELECT exercise FROM exercise WHERE level LIKE ?', (level,))
      print(c.fetchall())
      c.execute('SELECT * FROM exercise WHERE level LIKE ?', (level,))
      exercise_list = (c.fetchall())
      connection.commit()
      connection.close()
    else:
        for exercise in exercise_list:
            if narrow in exercise:
                print(exercise)
        


def u_l_c():
    print("Please enter the Upper/Lower/Compound you would like to search")
    u_l_c = "%" + input("Upper/Lower/Compound: ") + "%"
    print(f"Searching for {u_l_c} exercises")
    global exercise_list
    if search_count == 0:
      connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
      c = connection.cursor()
      c.execute('SELECT exercise FROM exercise WHERE u_l_c LIKE ?', (u_l_c,))
      print(c.fetchall())
      c.execute('SELECT * FROM exercise WHERE u_l_c LIKE ?', (u_l_c,))
      exercise_list = (c.fetchall())
      connection.commit()
      connection.close()
      search_count += 1
    else:
        for exercise in exercise_list:
            if narrow in exercise:
                print(exercise)
        search_count += 1
    connection.commit()
    connection.close()

def p_p():
    print("Please enter the Push/Pull you would like to search")
    p_p = "%" + input("Push/Pull: ") + "%"
    print(f"Searching for {p_p} exercises")
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    c.execute('SELECT * FROM exercise WHERE p_p LIKE ?', (p_p,))
    list = c.fetchall()
    print(c.fetchall())
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
    global search_count
    search_options()
    option = input("Option: ")
    if option == "1":
        muscle_group()
        search_count += 1
    elif option == "2":
        exercise()
        search_count += 1
    elif option == "3":
        level()
        search_count += 1
    elif option == "4":
        u_l_c()
        search_count += 1
    elif option == "5":
        p_p()
        search_count += 1
    elif option == "6":
        modality()
        search_count += 1
    elif option == "7":
        joint()
        search_count += 1
    elif option == "8":
        exit()
    else:
        print("Invalid option")
        search()         
    print("Would you like to narrow your search?")
    print("1. Yes")
    print("2. No")
    option = input("Option: ")   
    if option == "1":
        search()
    elif option == "2":
        exit()
    else:
        print("Invalid option")
        search()
    
    
    

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
    print("6. Modality")
    print("7. Joint")
    print("8. Exit")

filters_string = ""
filters = ""

def filter_by():
  global filters_string
  global filters
  narrow = False
  print("Would you like to filter by?")
  search_options()
  user_input = input("Option: ")
  if user_input == "1":
    if filters_string == "":
      print("Please enter the muscle group you would like to search")
      muscle_group = "%" + input("Muscle Group: ") + "%"
      filters_string = filters_string + "muscle_group LIKE ?" 
      filters = filters + "muscle_group"
    else:
      print("Please enter the muscle group you would like to search")
      muscle_group = "%" + input("Muscle Group: ") + "%"
      filters_string = filters_string + " AND muscle_group LIKE ?"
      filters = filters + "muscle_group"
  elif user_input == "2":
      exercise()
  elif user_input == "3":
    if narrow == False: 
      print("Please enter the level you would like to search")
      level = "%" + input("Level: ") + "%"
      filters_string = filters_string + "level LIKE ?"
      filters = filters + "level"
    elif narrow == True:
      print("Please enter the level you would like to search")
      level = "%" + input("Level: ") + "%"
      filters_string = filters_string + " AND level LIKE ?"
      filters = filters + "level"
  elif user_input == "4":
        u_l_c()
  elif user_input == "5":
        p_p()
  elif user_input == "6":
        modality()
  elif user_input == "7":
        joint()
  elif user_input == "8":
        exit()
  print("Would you like to narrow your search further?")
  print("1. Yes")
  print("2. No")
  option = input("Option: ")
  if option == "1":
    narrow = True
    filter_by()
  elif option == "2":
    print(f'SELECT exercise FROM exercise WHERE {filters_string}')
    print(filters)
    connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
    c = connection.cursor()
    #   c.execute('SELECT exercise FROM exercise WHERE muscle_group LIKE ?', (muscle_group,))
    c.execute(f'SELECT exercise FROM exercise WHERE {filters_string}', (filters,))
    print(c.fetchall())
    #   c.execute('SELECT * FROM exercise WHERE muscle_group LIKE ?', (muscle_group,))
    #   exercise_list = (c.fetchall())
    connection.commit()
    connection.close()
        


def program():
    greet()
    option = input("Option: ")
    if option == "1":
        filter_by()
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

# print(f'SELECT exercise FROM exercise WHERE {filters_string}')

# connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
# c = connection.cursor()
# c.execute('SELECT exercise FROM exercise')
# print(c.fetchall())

# print(search_count)