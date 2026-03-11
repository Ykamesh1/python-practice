# ----------------------------
# -- loop => while training --
# -- simple_password_guesss --
# ----------------------------

tries = 4 

mainpassword = "abcde"

inputpassword = input("type your password: ")

while inputpassword != mainpassword :
    
    tries -= 1 # tries = tries -1 
    
    print(f"wrong password, { "last" if tries == 0 else tries } chances left")
    
    inputpassword = input("type your password: ")
    
    if tries == 0 :
        
        print("all tries is finished")
        
        break      
    
        print("will not print")    
    
else:
    print("password is correct")    
    
    
    
    
    
    
    
    