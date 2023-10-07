#Datatypes in python
#Numeric Type

# 1) Integer

empId = 20
print(empId)
print(type(empId))

print()

Jerno = 7
print(Jerno)
print(type(Jerno))

# 2) Float
print()

price = 75.50
print(price)
print(type(price))

print()
#python madhe float madhe point natr 15 value print hotat
data = 45.77777777777733222222222222238828233233332
print(data)
print(type(data))

print()
# 3) Complex Number
# it is of the form a+bj where a is real no , b is imaginary no and j is suffix
complexData = (10+5j)
print(complexData)
print(type(complexData))
print()

# 4) Boolean
data1= True
print(data1)
print()
data2 = False
print(data2)
print(type(data2))
print()

x=10
y=20
print(x==y)
print()

ans = data1 + data2
print(ans)  # here ans is 1 becoz it return in 1 and 0 values in python

print()
 

# Sequence Type
# 1) String
 # string can be defined in three ways
Friend1="Amit"
print(Friend1)
print(type(Friend1))

print()

Friend2 = 'Harshada'
print(Friend2)
print()

Friend3 = """ Shiv """
print(Friend3)
print()

Friend4 = ''' Neha '''
print(Friend4)
print()


# 2) Range

x = range(10)
print(x)
print(type(x))

print()

for i in x:
    print(i)
    print()

# 3) List

lang = ["c", "python", "Java" , "Pyhton"]
buckelist = ["manali", "hotel", 2, "rgrgr", 4,4,3]
print(lang)
print()

print(buckelist)
print()

# list are mutable .i.e we can change the value in the list
lang[3] = "Harshda"
print(lang)
print()


# 4) Tuple

emptuple = (18, "Amit", 25.8, "hi", 8)
print(emptuple)
print(type(emptuple))

#tuble are immutable i.e we cannot change value in tuples

#emptuple[2] = "Ram"
#print( emptuple)  error
print()

# None type
x = None
print(x)
print(type(x))

# set Type

# set remove duplicate data and it is Immutable
print()
setdata = {10,20,23,3,342,2,23}
print(setdata)

#setdata[2] = 79
#print(setdata) error


#Dictionary(map) type

player = {7:"Mahi", 18:"Virat", 45:"Rahul"}
print(player)
print()


#Bytes Datatype

listdata=[10,20,30,40,50]
bytedata = bytes(listdata)
print(bytedata)
print(type(bytedata))
print()


# byte data chi range ( 0 to 255) aste ya pudhe jr data gela tr error yeto
#byte immutable ye apn value change ny kru shakt
# krycha asel tr apn bytearray use krto
bytesdata = bytearray(listdata)
for i in bytesdata:
    print(i)

