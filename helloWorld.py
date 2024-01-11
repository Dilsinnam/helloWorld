# A hashtag makes a comment
print(
    "Hello World"
)  # In the "" is a string literal, put what you want to print inside of that
# Setting and assigning variables
a = 15  # Assigning the value of 15 to A
b = 29
c = a + b
print(c)  # Printing just the letter allows for the variable to be called
print(
    "The value of a is",
    a,
    "The value of b is",
    b,
    "The value of a and b is",
    c,
)  # Comma, calling value c

# \n creates a new line, \t creates a tab of space
print("This is a", "\nnew line.")
print("This is a \t", "tab space.")

# / Divides, //removes all sig figs and rounds to the nearest whole number
# % Modular, finds the divisibility of a number by another number
d = 90
e = 80
f = e % d
print(f)  # 7, 24 later

# Order of functions is in P.E.M.D.A.S
g = 7
h = 24

h = 10  # Value of h gets updated because it is further down

g = h  # Both values become 10

h = g
h = 20

i = g + h
print(i)
