# Take input from the user and convert it to a list of integers
try:
    input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    # Define the lambda function to square a number
    square = lambda x: x ** 2
    
    # Use map to apply the lambda function to each element in the input list
    squared_list = list(map(square, input_list))
    
    # Output the squared list
    print("Square the elements of the list:")
    print(squared_list)
except ValueError:
    print("Invalid input. Please enter a valid list of integers separated by spaces.")
