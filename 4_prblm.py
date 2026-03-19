# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enetr a number"))
if n<2:
    print(f"{n} is not a prime number ")
else:
 for i in range (2,n):
    if (n%i)==0:
        print(f"{n} number is not prime")
        break
    
    else :
     print(f"{n} number is  prime ")