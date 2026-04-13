p=int(input("Enter Principal amount :"))
r=int(input("Enter Rate of interest :"))
t=int(input("Enter time period :"))
print("Simple Interest :",(p*r*t)/100.0) if 1<=p<=100000 and 1<=r<=20 and 1<=t<=10 else print("Invalid input")
