name=input("Enter the name of the person:")

age=int(input("Enter the age of the person:"))
print("Name:",name)
if age<=0:
  print("Age cannot be negative")
elif age>=18:
  print(name,"is eligible to vote")
else:
  print(name,"is not eligible to vote")
