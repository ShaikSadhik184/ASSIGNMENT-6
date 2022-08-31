#leap year
x=int(input("enter a year:"))
if x%400==0 or x%100!=0 and x%4==0:
    print("leap year")
else:
    print("non leap year")
    
