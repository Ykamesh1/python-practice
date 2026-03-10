# --------------------
# user_input_practical
# --------------------


fname = input("what\'s your firstname ?")
mname = input("what\'s your middlename ?")
lname = input("what\'s your lastname ?")

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()


print(f"hello {fname} {mname} {lname} happy to see you ")