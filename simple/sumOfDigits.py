n=int(input("Enter a number : "))
rev=0
t=n
l=0
for i in range(0,11):
   if t!=0:
      t//=10
      l+=1
if 1<=n<=1000000000:
   for i in range(0,l):
      if n!=0:
         rev+=n%10
         n//=10
      else:
         break
   print("Sum of digits:",rev)
else:
   print("Invalid input")
