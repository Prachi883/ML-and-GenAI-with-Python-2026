# Assignment 3 Solutions

# 1. Function to print first 10 natural numbers
def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

print_natural_numbers()


# 2. Function to calculate sum of first N natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("\nEnter value of N: "))
print("Sum of first", n, "natural numbers is:", sum_natural_numbers(n))


# 3. Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

num = int(input("\nEnter a number to reverse: "))
print("Reversed Number:", reverse_number(num))


# 4. Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

num = int(input("\nEnter a number to count digits: "))
print("Number of digits:", count_digits(num))


# 5. Function to check palindrome number
def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

num = int(input("\nEnter a number to check palindrome: "))
palindrome(num)


# 6. Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()

n = int(input("\nEnter number of terms for Fibonacci series: "))
fibonacci(n)


# 7. Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))

elif choice == 2:
    print("Result:", subtract(num1, num2))

elif choice == 3:
    print("Result:", multiply(num1, num2))

elif choice == 4:
    if num2 != 0:
        print("Result:", divide(num1, num2))
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid Choice")


# 8. Create a text file and store student details
file = open("student.txt", "w")

name = input("\nEnter student name: ")
marks = input("Enter student marks: ")

file.write("Student Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Student details stored successfully.")


# 9. Read data from a file
file = open("student.txt", "r")

print("\nReading Student File:")
print(file.read())

file.close()


# 10. Handle division by zero using exception handling
try:
    a = int(input("\nEnter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


# 11. Create a Student class with name and marks
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("\nEnter student name: ")
marks = int(input("Enter student marks: "))

s1 = Student(name, marks)
s1.display()