"""
Description:

Case Closed?

Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file
objects open, and if we're not careful, they won't all be closed. How can we test this?

f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True

Python file objects have a closed attribute which is True when the file is closed and False otherwise.

By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.

Challenge:
Below your with...as code, do two things:

    1.Check if the file is not .closed.
    2.If that's the case, call .close() on it.
    3.(You don't need an else here, since your if statement should do nothing if .closed is True.)
    4.After your if statement, print out the value of my_file.closed to make sure your file is really closed.
"""
with open("text.txt", "w") as my_file:
    my_file.write("This is awesome")

    if my_file.closed != True:
        print my_file.close()
        print my_file.closed