# -------------
# -- practical membership control -- 
# --------------

# list contains admins
admins = ["ahmed", "osama", "sameh", "manal", "rahma", "mahmoud", "enas"]

#login

name = input("please type your name").strip()

# if name is in admin
if name in admins:
    
   print(f"hello {name} welcome back ") 
   
   option = input("delete or update your name ?").strip()
   
   
   # update option
   if option == "update" or option ==  "u":
       
       thenewname = input("your new name please ").strip()
       
       admins[admins.index(name)] = thenewname
       
       print("name updated.")
       
       print(admins)
       
       # delete option
       
   elif option == "delete" or option == "d" :
       
       admins.remove(name)
       
       print("name deleted")
       
       print(admins)
       
    # wrong option 
    
   else: 
       print("wrong option choosed")   
          
   
else:
    
    status = input("not admin add you Y, N ?").strip().capitalize()
    
    if status == "Yes" or status == "Y":
        
        print("you have been added")
        
        admins.append(name)
        
        print(admins)
        
    else:
        print("you are not added")    
