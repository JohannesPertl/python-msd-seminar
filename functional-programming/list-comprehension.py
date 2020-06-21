numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers = list(range(20))


even = [x for x in numbers if x % 2 == 0]
print(even)


squares = [x*x for x in numbers]
print(squares)