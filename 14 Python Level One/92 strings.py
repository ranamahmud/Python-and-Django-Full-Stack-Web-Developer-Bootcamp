'hello'
"Hello"

"I'm a dog."

my_strings = 'abcdefg'
print(my_strings)
print(my_strings[-1])
print(my_strings[3])
print(my_strings[2:])
print(my_strings[4:])
print(my_strings[:4])
print(my_strings[2:5])
print(my_strings[::2])
x = my_strings.upper()
print(x)
print(my_strings.lower())
print(my_strings.capitalize())
my_strings = "Hello World"
print(my_strings.split(' '))

x = "Insert another string here: {}".format("Insert Me")
print(x)
x = "Item One: {}, Item Two: {}".format("dog", "cat")
print(x)
x = "Item One: {y}, Item Two: {x}".format(x="dog", y="cat")
print(x)