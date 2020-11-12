astring = "Hello world!"
s = "Strings are awesome!"

print(astring)
print("---------------------------")
#จำนวนตัวหนังสือข้อความ
print(len(astring))
print(len(s))
print("Length of s = %d" % len(s))
print("---------------------------")
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))

# เริ่มต้นด้วย0นับไปถึง O ตัวแรกได้้ค่า = 4
print(astring.index("o"))
print(astring.count("l"))
print("---------------------------")
print(astring[3:7])
print(astring[3:7:2])
print(astring[::-1])
print("---------------------------")
print(astring.upper())
print(astring.lower())
print("---------------------------")
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

print("---------------------------")
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("---------------------------")
# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())
print("---------------------------")
# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())
print("---------------------------")
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))