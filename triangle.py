print("in the name of Allah")

print("lets check that what numbers can be triangle")

numb1 = float(input("enter numb1 : "))
numb2 = float(input("enter numb2 : "))
numb3 = float(input("enter numb3 : "))

if numb1 < numb2+numb3 :
    check = " we can have a triangle"
else:
    check = "we cant have a triangle"
    
if numb2 < numb1+numb3 :
    check = "we cna have a triangle"
else:
    check = "we cant have a triangle"

if numb3 < numb1+numb2 :
    check = "we can have a triangle"
else:
    check = "we cant have a triangle"

print(check)