n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
n3=int(input("Enter third number :"))
print("Largest : ",n1) if n1>=n2>=n3 or n1>=n3>=n2 else print("Largest : ",n2) if n2>=n3 else print("Largest : ",n3)
