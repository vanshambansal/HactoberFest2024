def generate_pascals_triangle(n):
    # Create an empty list to store all the rows
    triangle = []

    # Loop over the number of rows
    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Calculate the values for the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle

def print_pascals_triangle(triangle):
    n = len(triangle)
    
    # Print each row of the triangle
    for i in range(n):
        # Print leading spaces for alignment
        print(' ' * (n - i), end='')

        # Print the values in the row
        for num in triangle[i]:
            print(num, end=' ')
        
        print()  # Move to the next line after each row

# Get the number of rows for the Pascal's triangle
n = int(input("Enter the number of rows: "))

# Generate and print Pascal's Triangle
triangle = generate_pascals_triangle(n)
print_pascals_triangle(triangle)
