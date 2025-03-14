print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

choice = int(input("Enter the number corresponding to your choice: "))

if choice in [1, 3, 4, 6, 7]:
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5]:
    size = int(input("Enter the size of the square/rectangle: "))
elif chоice == 8:
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

print(" ")

if choice == 1:  # Right-angled Triangle
    for i in range(1, rows + 1):
        print("*" * i)
    print(" ")
    pass

elif choice == 2:  # Square with Hollow Center
    print("*" * size)
    for i in range(1, size - 1):
        if i == 0 or i == -1:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")
    print("*" * size)
    pass

elif choice == 3:  # Diamond
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end = "")

        for k in range(2 * i + 1):
            print("*",end = "")

        print()

    for i in range(rows - 2, -1, -1):
        for j in range(rows - i - 1):
            print(" ", end = "")

        for k in range(2 * i + 1):
            print("*", end="")

        print()
    pass

elif choice == 4:  # Left-angled Triangle
    for i in range(rows, 0 , -1):
        print("*" * i)
    pass

elif choice == 5:  # Hollow Square
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")
    pass

elif choice == 6:  # Pyramid
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end = "")

        for k in range(2*i + 1):
            print("*",end = "")

        print()
    pass

elif choice == 7:  # Reverse Pyramid
    for i in range(rows - 1, -1, -1):
        for j in range(rows - i - 1):
            print(" ", end = "")

        for k in range(2 * i + 1):
            print("*", end="")

        print()
    pass

elif choice == 8:  # Rectangle with Hollow Center
    for i in range(height):
        if i == 0 or i == height - 1:
            print("*" * width)
        else:
            print("*" + " " * (width - 2) + "*")
    pass

else:
    print("❌ Invalid choice! Please restart the program.")
