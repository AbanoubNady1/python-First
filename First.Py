
# type Showing Data type


if True:  
    print("Python")
    print("Programming")

print(type(100))
print(type(100.1))

name = "Hello"
myName = "Hello"
my_name = "Hello"


print(name)
print(myName)
print(my_name)

x = 10
x = "Welcome"
print(x)

help("keywords") #Resrved Words

L, M, N= 1, 2 ,3
print(L,M,N)

#009

# Back Space
print("hello\bWorld")


#Escpe New Line +\
print("Hello \
    I Love \
    Python")


print(" Back Slach\"")
print(" Back Slach\\")
print('Back Slach \"test"')

#Line Feed
print("Hello World\nSecondline")

#Carriage Return
print("Hello World\rSecondline")
print("123456\rABCD")

#Horizontal Tab
print("Hello\t World")

#xhh Character Hex Value (Searche in goolgle letter hex value)
print("\x4F\x73")
print("test")

#010

sheep = "Elshekh"
lang = "Olla"
print(sheep + " " + lang)

full = sheep + " " + lang
print(full)


A = "First \
Second \
Third"

B ="A \
B \
C"

print(A+"\n"+B)

#011

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour =  "This is Double Quotes 'test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second "SSSSS"
Third'''


myStringSix = """First
Second 'SSSSS' "TTTTTTTTT"
Third"""

print(myStringFive)
print(myStringSix)

#012

#index
myString = "I Love Python"

print(myString[0])
print(myString[-9])

#slicing[Start:End(end not included)]/[Start:End:Steps]

print(myString[7:13])
print(myString[5:])
print(myString[:])

print(myString[::1])
print(myString[::2])
print(myString[::3])

#013 
#strip
a = "#@    I Love Python    @#"
print(a.strip("@#"))
print(a.rstrip())
print(a.lstrip())
print(len(a.lstrip()))

#title()

b = "I Love 2d Graphics and 5G technology"
print(b.title())

#capitalize()
b = "I Love 2d Graphics and 5G technology"
print(b.capitalize())

#zfill
c,d,e,f = "1","11","111","1111"
print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#Upper()
m= "Bebo"
print(m.upper())

#ULower()
m= "Bebo"
print(m.lower())

#014
#split()  rsplit()

n = "Welcome BBBB ppppppp yyyyyyyyy"
print(n.split())

h = "Welcome-BBBB-ppppppp-yyyyyyyyyy"
print(h.split("-"))

u = "Welcome-BBBB-ppppppp-yyyyyyyyyyyy"
print(u.split("-", 2))

j = "Welcome-BBBB-ppppppp-yyyyyyyyyyyy"
print(j.rsplit("-", 2))

# center()

y = "Bebo"
print(y.center(20,))
print(y.center(20, "$"))

# count()

p = "I love Python and Php Cause Php Is Diff"
print(p.count("Php"))
print(p.count("Php", 0, 25)) #start, end

# swapcase()

g= "I Love Python"
k= "i Love python"

print(g.swapcase())
print(k.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("P",7 ,12))


# endswith()
print(i.endswith("n"))

#015
#index(SubString, Start, End)

o = "I Love Python"
print(o.index("P"))
print(o.index("P", 0, 10))
#print(o.index("P", 0, 10)) Through ERORR

#find(SubString, Start, End)

v = "I Love Python"
print(v.find("P"))
print(v.find("P", 0, 5))

#rjust(width, Fill char) ljust(width, Fill char)

t = "Bebo"
print(t.rjust(10, "%"))
print(t.ljust(10, "%"))

#splitline()
e = """First Line
Second Line
Third Line""" 

print(e.splitlines())
print(type(e.splitlines()))

#expand tabs()

g = "Hello\tWorld\tWelcome"

print(g.expandtabs(5))

one = "I Love Python And #G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five= "i love python"
six= "I Love Python"
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaaBbbbbb"
y = "AaaaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaaaBbbbbb"
z = "AaaaaaaBbbbbb111#"
print(u.isalnum())
print(z.isalnum())

#016

#replace(Old Value, New Value, Count)
a ="Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Itreble)

myList = ["Osama", "Elzero", "Web"]
print("-".join(myList))
print("   2".join(myList))
print(type("   2".join(myList)))

#017

name = "Bebo"
age = 18
rank = 1

print("My Name is: " + name)
#print("My Name is: " + name + " and My Age is: " + age) #Type Error
print("My Name is: %s" % name)
print("My Name is: %s and My Age is %s" %(name, age)) 
print("My Name is: %s, My Age is: %d and My Rank is: %f" %(name, age, rank))

print("My Rank is: %.2f" % rank)

# %s => String
# %d => Number
# %f => Float


myLongString = "Hello Welcome Peoples Hello Hello"
print ("Messege is %.5s" % myLongString)
print ("Messege is %s" % myLongString)
#Hello
#Welcome
