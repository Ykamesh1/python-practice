# ------------------------------------------
# calculate age advanced version and training 
# -------------------------------------------

# write note 

print("#" * 80 )
print("you can write the first letter or the full name of the time unit".center(80, "#" ))
print("#" * 80)

# collect age data

age = input("please write your age ").strip()

# collect time unit data

unit = input("please choose time unit : months, weeks , days").strip().lower()


# get time unit

months = int(age) * 12
weeks = months * 4 
days = int(age) * 365

if unit == "months" or "m":
    print("you choosed the unit months")
    print(f"you lived for {months:,} months.")
    
elif unit == "weeks" or "mw":
    print("you choosed the unit weeks")
    print(f"you lived for {weeks:,} weeks.")
    
elif unit == "days" or "d":
    print("you choosed the unit days")
    print(f"you lived for {days:,} days.")    

