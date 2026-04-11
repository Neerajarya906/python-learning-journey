# 1. Write a program using functions to find greatest of three numbers. 

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :  
        return c
a = float(input("Enter a number "))
b = float(input("Enter a number "))
c = float(input("Enter a number "))
print(f"the greatest number is {greatest(a,b,c)}")
