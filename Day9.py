# Description: Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
# if a year divide by 4 and 100 then year also must be divide by 400 

def is_leap(year): # created a function 
    if year % 4 == 0: # 
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else:
            return True
    else:
        return False

# Testing the function
year=int(input("Enter a year: "))  
print(is_leap(year)) # True # calling the function
