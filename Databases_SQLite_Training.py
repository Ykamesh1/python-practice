# -----------------------------------------------------------------
# -- databases => SQLite => training on most things i have learned --
# ------------------------------------------------------------------


import sqlite3

def get_all_data():
    
     try:
        
         # connect to database 
         db = sqlite3.connect("app.db")
        
         # print success msg
         print("connected to database successfully ")
        
         # setting up the cursor
         cr = db.cursor()
        
         # fetch data from database
         cr.execute("select * from users")
        
         # assign data to variables
         results = cr.fetchall()
         
         # print number of rows
         print(f"database has {len(results)} rows")
         
         # printing msg
         print("showing data:")
         
         # loop on results
         for row in results:
             
             print(f"UserID => {row[0]}", end=" ") 
             
             print(f"Ussername=> {row[1]}") 

   
     except sqlite3.Error as er:
        
         print(f"Error reading data {er}")    
    
    
     finally:
         
         if (db):
             
             # close database connection
             db.close()
             
             print("connection database is closed")
             
             
get_all_data()

    
 