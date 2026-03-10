# -------------------------------
# practical your age full details
# -------------------------------

# input age

age = int(input("what\'s your age"))

# get age in all time

months = age * 12
weeks = months * 4 
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60 


print("you lived for: ")
print(f"{months} months.")
print(f"{weeks:,} weeks.")
print(f"{days:,} days.")
print(f"{hours:,} hours.")
print(f"{minutes:,} minutes.")
print(f"{seconds:,} seconds.")




