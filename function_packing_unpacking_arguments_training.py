# -----------------------------------------------------
# -- function packing, unpacking arguments trainings --
# -----------------------------------------------------

mytuple = ("html", "css", "js")
 
myskills = {
    "go" : "80%", 
    "python" : "90%",
    "mysql" : "60%"
}



def show_skills(name, *skills, **skillswithprogres):
    
    print(f"hello {name}\nskills without progress is: ")
    
    for skill in skills:
        
        print(f"- {skill}")
        
    print("skills with progress is: ")
    
    for skill_key, skill_value in skillswithprogres.items():
        print(f"- {skill_key} => {skill_value} ")
    
show_skills("ykamesh", *mytuple , **myskills)    