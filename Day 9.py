# Loop Control Statements
# break, continue, pass



# 1. BREAK STATEMENT
# break completely stops the loop.

print("----- BREAK EXAMPLE -----")

for i in range(1, 6):
    if i == 4:
        break
    print(i)


# 2. CONTINUE STATEMENT
# continue skips the current iteration.

print("\n----- CONTINUE EXAMPLE -----")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 3. PASS STATEMENT
# pass does nothing and allows the program to continue.

print("\n----- PASS EXAMPLE -----")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# 4. BREAK WITH WHILE LOOP

print("\n----- BREAK WITH WHILE LOOP -----")

i = 1

while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1


# 5. CONTINUE WITH WHILE LOOP

print("\n----- CONTINUE WITH WHILE LOOP -----")

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)


# 6. SKIP EVEN NUMBERS USING CONTINUE

print("\n----- SKIP EVEN NUMBERS -----")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# 7. BREAK WITH USER INPUT

print("\n----- BREAK WITH USER INPUT -----")

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    print("You entered:", num)


# 8. PASS IN A FUNCTION

def future_function():
    pass


print("\nProgram completed successfully!")
