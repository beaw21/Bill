mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
print("----------------")
print(mylist[0])
print(mylist[1])
print(mylist[2])
print("----------------")
for x in mylist:
    print(x)
print("----------------")
mylist1 =[1,2,3]
print(mylist1)
print("----------------")
print(mylist1[1])
print("----------------")

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)