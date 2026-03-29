# -------------------------------------
# --     exceptions handling   --
# --  try | except | else | finally  --
# --       advanced example        --
# -------------------------------------

the_file = None
the_tries = 5 

while the_tries > 0:
    
    try:       #try to open the file
      
        print("enter the file name with absolute path to open")
        
        print(f"you have {the_tries} tries left")
        
        print("example : D:\\python\\files\\yourfile.extension")
        
        fime_name_and_path = input("file name => : ").strip()
        
        the_file =open(fime_name_and_path, "r")
        
        print(the_file.read())
        
        break

    except FileNotFoundError:
        
        print("file not found be sure the name is valid")    
    
        the_tries -= 1
        
    except :
        
        print("error happened")    
    
    finally:
        
        if the_file is not None :
        
               the_file.close()
        
               print("the file is closed")
      
else :
    
    print("all tries is done")
