c=input("Enter a Alphabet :")
print(c," is Vowel") if c in "aeiouAEIOU" else print(c," is Consonant") if c.isupper() or c.islower() else print(c,"is Number or Special character")
