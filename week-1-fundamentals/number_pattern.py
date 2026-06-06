name = input("Enter Your name :")
number = int(input("Enter a starting number: "))
count = int(input("Enter how many numbers:"))

numbers = [ ]
for i in range (count):
	numbers.append(number+i)


print(f" hello {name}")
print(f"pattern: {numbers}")
print(f"sum: {sum(numbers)}")
print(f"average:{sum(numbers)/len(numbers)}")
