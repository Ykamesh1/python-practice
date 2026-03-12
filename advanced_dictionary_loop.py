# ------------------------------
# -- advanced dictionary loop --
# ------------------------------

myskills ={
    "html": "80%",
    "css": "90%",
    "js": "70%",
    "php": "80%"       
}

print(myskills.items())

for skills in myskills:
    print(f"{skills} = > {myskills[skills]}" )



for skill_key, skill_progress in myskills.items():
    
     print(f"{skill_key} = > {skill_progress}" )

myultimateskills = {
    "html": {
        "main": "80%",
        "pugjs": "80%"    
    },
    "css":{
        "main": "90%",
        "sass": "70%"
    }   
}

for main_key, main_value in myultimateskills.items():
    
    print(f"{main_key} progress is: " )
    
    for child_key, child_value in main_value.items():
        
        print(f"-{child_key} = > {child_value}")
    