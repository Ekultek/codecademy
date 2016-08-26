# Anonymous functions
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# Lambda syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == 'Python', languages)

# Try it!
squares = [x**2 for x in range(1, 11)]
print filter(lambda x: 30 <= x <= 70 , squares)

# Lambda expressions
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x.replace('X', ""), garbled)
print message