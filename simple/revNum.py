n=int(input("Enter a number : "))
rev,t,l=0,n,0
for i in range(0,11):
   if t!=0:
      t//=10
      l+=1
if 1<=n<=1000000000:
   for i in range(0,l):
      if n!=0:
         rev+=(n%10)*(10**(l-i-1))
         n//=10
      else:
         break
   print("Reverse of the number:",rev)
else:
   print("Invalid input")
