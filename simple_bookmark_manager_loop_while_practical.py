# ---------------------------
# --loop => while training --
# -- simple_bookmark_manage --
# ----------------------------

# empty list to fill later
myfavouritewebs =  []

# maximum allowed websites
maximumwebs = 5

while maximumwebs > 0 :
    
    # input the new website
    web = input("website name without https:// ")
    

    # add the new website to the list
    myfavouritewebs.append(f"https://{web.strip().lower()}")
    
    # decrease one number from allowed websites
    maximumwebs -= 1  # maximumwebs = maximumwebs - 1
    
    # print the add messege
    print(f"website added, {maximumwebs} places left")
    
    # print the list
    print(myfavouritewebs)

else: 
    
    print("bookmark is full, you cant add more")     
    
 # check if list is not embty
if len(myfavouritewebs) > 0 :
     
     
      # sort the list
    myfavouritewebs.sort()
       
    index = 0 
       
    print("printing the list of websites in your bookmark ")
    
    while index < len(myfavouritewebs) :
        
        print(myfavouritewebs[index])
        
        index += 1 # index = index +1 
        
        
          
       
       
       
       
       