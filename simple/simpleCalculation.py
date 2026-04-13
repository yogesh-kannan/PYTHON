n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
print("-----menu------\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
op=int(input("Enter your choice : "))
match op :
   case 1:
      print("Addition : ",n1+n2)
   case 2:
      print("Subtraction : ",n1-n2)
   case 3:
      print("Multiplication : ",n1*n2)
   case 4:
      print("Division : ",1.0*n1/n2)
   case _:
      print("Invalid choice ")
