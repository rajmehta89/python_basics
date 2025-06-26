print("hell0")

name="raj"
print("my name is", name)

age=input("Enter your age: ")
print("Your age is", age)

if age.isdigit() and int(age) >= 18:
    print("You are an adult.")
else:    print("You are not an adult.")
print("Thank you for using the program!")

for i in range(5):
    print("This is iteration number", i + 1)
print("Goodbye!")
# This is a simple Python script that prints a greeting, takes user input, and checks if the user is an adult.
# It also includes a loop that prints a message multiple times.

i = 0
while i < 5:
    print("This is iteration number", i + 1)
    i += 1
    print("Goodbye!")

def greet(name):
    print("Hello,", name)

greet("Raj")


list_a=["raj", "john", "doe",11, 12.5]
print("List of names:", list_a)

list_a.append("alice")
print("Updated list of names:", list_a)
list_a.remove("john")
print("List after removing 'john':", list_a)

tuple = ("raj", "john", "doe",11, 12.5)
print("Tuple contents:", tuple)

for name in tuple:
    print("Hello,", name)

# tuple.append("alice")  # Tuples are immutable, so this will raise an error

for name in list_a:
    print("Hello,", name)

dict = {"name": "Raj", "age": 30, "city": "New York"}
print("Dictionary contents:", dict)

for key, value in dict.items():
    print(f"{key}: {value}")

print("set example")
set={1,2,3,3}
print("Set contents:", set)
set.add(4)
print("Set after adding 4:", set)

frozenset = frozenset([1, 2, 3, 4])
print("Frozenset contents:", frozenset)
# frozenset.add(5)  # This will raise an error because frozensets are immutable

for i in frozenset:
    print("Frozenset element:", i)
print("End of the script.")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Raj", 30)
person1.greet()

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print(f"The {self.species} makes a sound.")

animal1 = Animal("Dog")
animal1.make_sound()    

class Engine:
    def __init__(self, power):
        self.power = power

    def show_power(self):
        print("Engine power is:", self.power)

class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object passed here

    def show_engine_info(self):
        self.engine.show_power()  # Call method from Engine class

# Create Engine object
e1 = Engine("150 HP")

# Pass it to Car
c1 = Car(e1)
c1.show_engine_info()



#here teh calss member will be shared by all instances of the class
# Instance data members are unique to each instance of the class.

class Employee:
    company = "TCS"  # ← Class data member

    def __init__(self, name):
        self.name = name  # ← Instance data member

e1 = Employee("Raj")
e2 = Employee("Meena")

print(e1.name)      # Raj
print(e2.name)      # Meena
print(e1.company)   # TCS (shared)
print(e2.company)   # TCS (same for all)


# Using f-strings for formatted output
name = "Raj"
age = 25
print(f"My name is {name} and I am {age} years old.")


# Using str.format() for formatted output

name1 = "Raj"
age1 = 25
print("My name is {} and I am {} years old.".format(name1, age1))
print("My name is {0} and I am {1} years old.".format(name1, age1))
print("My name is {n} and I am {a} years old.".format(n=name1, a=age1))


# Using the % operator for formatted output
name2 = "Raj"
age2 = 25
print("My name is %s and I am %d years old." % (name2, age2))

#now try-expect
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("That's not a valid number! Please enter a valid integer.")

#now work with the file system
import os

os.makedirs("my_directory", exist_ok=True)  # Create a directory if it doesn't exist
with open("my_directory/my_file.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file was created using Python.\n")


with open("my_directory/my_file.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
# Clean up by removing the file and directory
os.remove("my_directory/my_file.txt")   
os.rmdir("my_directory")  # Remove the directory (it must be empty)    


#practise of the lamba fucntion
add=lambda x,y:x+y
print("Sum using lambda function:", add(5, 10))

#it is like importing the module here
#this way we can import and then use the module
import math
print(math.sqrt(16))

#now map/filter/reduce
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))
print("Squared numbers using map:", squared_nums)

#now filetr into the even numbers
evens=list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", evens)

print("the evens list is", evens)
print("the normal list is this", nums)

#now work with the boolean operators here
x=9
y=5

print("Boolean operations:")
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT
print(x > y)  # Greater than
print(x < y)  # Less than
print(x == y)  # Equal to

#now what is enumarator means 
#it simply means loop woth the index here 
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
    