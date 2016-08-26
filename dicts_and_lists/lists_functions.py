# Comprehensions
even_squares = [x**2 for x in range(1, 11) if (x**2) % 2 == 0]
print even_squares

# Try it yourself!
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]
print cubes_by_four

# Slicing
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]

# Reversing a list
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]

# Stride length
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# Comprehending Comprehensions
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives

# List slicing!
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
forward = garbled[::-1]
message = forward[::2]
print message

