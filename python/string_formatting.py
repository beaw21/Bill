name = "John"
print("Hello, %s!" % name)
print("---------------------")

age = 23
print("%s is %d years old." % (name, age))
print("---------------------")

mylist = [1,2,3]
print("A list: %s" % mylist)
print("---------------------")

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)