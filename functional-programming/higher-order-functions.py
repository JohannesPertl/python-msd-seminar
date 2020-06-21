# Higher oder function:
#   a function that takes a function as an argument, or returns a function


def shout(text):
    print(text.upper())


shout('Hello')

# Assigning function to a variable
yell = shout  # Notice: No parentheses

yell('Hello')


def whisper(text):
    print(text.lower())


def greet(func):
    func("Hi, I am created by a function passed as an argument.")


greet(shout)
greet(whisper)
