
"""
Line 1 of block comment
Line 2 of block comment
Line 3 of block comment
"""
"""
A condition is a comparison.
Conditions evaluate a boolean value to be true or false.
If a condition is true, the following block of code will run.
A block of code will be indented

COMPARISONS:
>    Greater Than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
==   Equal to
!=   Not equal to

"""

mark = int(input("Please enter your test mark: "))

if mark >= 90:
    print ("You aced it!")
    
elif mark >= 70:
    print ("You got a B! Good Job!")

elif mark >= 60:
    print("That's a C!")
    
elif mark >= 50:
    print("You barely made it!")
    
else:
    print("You failed!")
    
if (mark >= 0 and mark <= 100):
    print("You have a valid mark")
    
if (mark > 100 or mark < 0):
    print("This is an invalid mark")