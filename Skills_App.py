# ----------------------------------------------------
# -- database => SQLite => create skills --
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create Database and connet
db = sqlite3.connect("app.db")

# setting up the cursor
cr = db.cursor()


def commit_and_close():
    """Commit Changes And Close Connection To Database"""
    db.commit()  # save commit
    db.close()  # close database
    print("connection to database is closed")
    

# my user id
uid = 1


# input big message

input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress"
"q" => Quit The App
Choose Option: 
"""
# input option choose
user_input = input(input_message).strip().lower()

# command list
commands_list = ["s", "a", "d", "u", "q"]

# define the methods
def show_skills():
    
    cr.execute(f"select * from skills where user_id = '{uid}'")
    
    results = cr.fetchall()
    
    print(f"You Have {len(results)} Skills")
    
    if len(results) > 0:
        
        print("Showing Skills With Progress: ")
    
    for row in results:
        
        print(f"Skill => {row[0]}", end=" ")
        
        print(f"Progress => {row[1]}%")


    commit_and_close()

def add_skill():
    
    sk = input("Write Skill Name: ").strip().capitalize()
    
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    
    results = cr.fetchone()
    
    if results == None: # there is no skill with this name in database
        
         prog = input("Write Skill Progress: ").strip()
    
         cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
        
    else: # there is a skill with this name in databse
            
            user_choice = input(f"Do You Want To Update Progress? Y\\N: ")
            
            if user_choice == "y":
    
                 prog = input("Write The new Skill Progress: ").strip()
    
                 cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
            
            else:
                print("Update Cancelelled")
            
           
    commit_and_close()
    
def delete_skill():
    
   sk = input("Write Skill Name: ").strip().capitalize()
        
   cr.execute(f"delete from skills where name = '{sk}'and user_id = '{uid}'")
   
   commit_and_close()
 

def update_skill():
    
    sk = input("Write Skill Name: ").strip().capitalize()
    
    prog = input("Write The new Skill Progress: ").strip()
    
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
    
    commit_and_close()           

# check if command is exists
if user_input in commands_list:
    
    
    if user_input == "s":
        
        show_skills()
        
    elif user_input == "a":
        
        add_skill()
        
    elif user_input == "d":
        
        delete_skill()
    
    elif user_input == "u":
        
        update_skill()  
          
    else:
        print("App Is Closed.")
        
        commit_and_close()
              
else:
    print(f"Sorry This Command \"{user_input}\" Is Not Found")    