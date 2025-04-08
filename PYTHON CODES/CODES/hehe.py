rows = 3  # Number of rows in the triangle

# Initialize a list of numbers to use
numbers = [1, 2, 3, 4, 5, 6]

index = 0  # Index for accessing elements in the list
for i in range(1, rows + 1):  # Loop through each row
    for j in range(i):  # Loop through each column in the row
        if index < len(numbers):  # Ensure we do not exceed the list length
            print(numbers[index], end=" ")  # Print the number
            index += 1
    print()  # Newline for the next row
