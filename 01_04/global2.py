name = "Susan"
print(name)


def print_name():
    global name
    name = "Peter"
    print(name)


print_name()
print(name)
