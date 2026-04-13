n=int(input("Enter a number : "))
fact=1;
if 1<=n<=12:
   for i in range(1,n+1):
      fact*=i
   print("Factorial of",n,"Numbers :",fact)
else:
   print("Invalid input")
