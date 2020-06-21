# Higher oder function:
#   a function that takes a function as an argument, or returns a function


def shout(text):
    return text.upper()


print(shout('Hello'))

# Assigning function to a variable
yell = shout  # Notice: No parentheses

print(yell('Hello'))
