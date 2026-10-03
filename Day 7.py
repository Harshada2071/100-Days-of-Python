# Problem 1: Add Two Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2

print("Sum:", sum_result)


# Problem 2: Find Even or Odd

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Problem 3: Find Largest of Two Numbers

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First number is larger.")
elif num2 > num1:
    print("Second number is larger.")
else:
    print("Both numbers are equal.")


# Problem 4: Check Positive, Negative or Zero

number = float(input("\nEnter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Problem 5: Check Voting Eligibility

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Problem 6: Calculate Grade

marks = float(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")


# Problem 7: Simple Calculator


num1 = float(input("\nEnter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")


# Problem 8: Check Number in Range

number = float(input("\nEnter a number: "))

if number >= 10 and number <= 50:
    print("The number is between 10 and 50.")
else:
    print("The number is outside the range.")


# Problem 9: Check Login

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid username or password.")


# Problem 10: Assignment Operator Practice

number = 10

print("\nOriginal number:", number)

number += 5
print("After += 5:", number)

number -= 2
print("After -= 2:", number)

number *= 2
print("After *= 2:", number)

number /= 2
print("After /= 2:", number)

