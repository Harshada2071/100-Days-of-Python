# 1. Basic Nested Loop
# A loop inside another loop is called a nested loop.

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 2. Understanding Rows and Columns
# Outer loop = Rows
# Inner loop = Columns


for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()


# 3. Square Pattern

for row in range(5):
    for column in range(5):
        print("*", end=" ")
    print()


# 4. Right-Angled Triangle Pattern


for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()

# 5. Number Pattern


for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()

# 6. Same Number in Each Row

for row in range(1, 6):
    for column in range(row):
        print(row, end=" ")
    print()

# 7. Alphabet Pattern

for row in range(1, 4):
    for column in range(row):
        print("A", end=" ")
    print()


# 8. Multiplication Table using Nested Loop


for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


