"""
Desciption:

Reading

Excellent! You're a pro.

Finally, we want to know how to read from our output.txt file. As you might expect, we do this with the read()
function, like so:

print my_file.read()

Challenge:

    1.Declare a variable, my_file, and set it equal to the file object returned by calling open() with both
      "output.txt" and "r".
    2.Next, print the result of using .read() on my_file, like the example above.
    3.Make sure to .close() your file when you're done with it! All kinds of doom will happen if you don't.
"""
my_file = open("output.txt", "r+")
print my_file.read()
my_file.close()

"""
output.txt:
1
4
9
16
25
36
49
64
81
100

None
"""