"""
Description:

Just a Little BIT

Welcome to an intro level explanation of bitwise operations in Python!

Bitwise operations might seem a little esoteric and tricky at first, but you'll get the hang of them pretty quickly.

Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits,
a series of zeros and ones. In fact, pretty much everything in a computer is represented by bits. This course will
introduce you to the basic bitwise operations and then show you what you can do with them.

Bitwise operators often tend to puzzle and mystify new programmers, so don't worry if you are a little bit confused at
first. To be honest, you aren't really going to see bitwise operators in your everyday program. However, they do pop up
from time to time, and when they do, you should have a general idea of what is going on.

Challenge:
In the editor are the 6 basic bitwise operations. Click Save & Submit Code and see what the console prints out.
All of them will be explained in due time!
"""
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT


"""
Output:
0
10
0
13
38
-89
None
"""