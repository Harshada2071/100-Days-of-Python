# 1. if Statement
age = 20

if age >= 18:
    print("You are eligible to vote.")


# 2. if-else Statement

number = 10

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 3. if-elif-else Statement

marks = 75

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


# 4. Multiple Conditions

temperature = 30

if temperature > 35:
    print("It is very hot.")
elif temperature >= 25:
    print("The weather is warm.")
else:
    print("The weather is cool.")


# 5. Nested if Statement

age = 20
has_id = True

if age >= 18:
    print("You are an adult.")

    if has_id:
        print("You can enter.")
    else:
        print("ID is required.")
else:
    print("You are not eligible to enter.")


# 6. Real-Life Example

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")
