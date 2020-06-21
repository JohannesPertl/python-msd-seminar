# Lambda
double = lambda x: x * 2

print(double(2))

# Filter
# Filter takes a function and a list as arguments

numbers = list(range(20))

even_numbers = list(filter(lambda x: (x % 2 == 0), numbers))

print(even_numbers)
