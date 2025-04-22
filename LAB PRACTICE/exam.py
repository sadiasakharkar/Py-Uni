# #rule 1: combination of A-Z a-z 0-9 _
# sadia = 10
# SAdia = 10
# Sadia12 = 10

# # rule 2 : can write multiple words sepreted by _
# sadia_lavesh = 10

# # rule 3 : should start with a letter or _ 
# sadiaaa = 10
# _sadiaaa = 10

# # rule 4 : can be as long  as you want
# sadia_lavesh_123cbshbjhdsbfbhsbfj = 10

# # # rule 5 : can not start with a number
# # sadia lavesh = 10
# # 66 

# # rule 6 :  can not use keywords as identifier name
# # def class for while if else pass continue return break (keywords)

# # rule 7 : can not use special characters
# # @ $%^&*() cannot be used as identifier name 

# # rule 8  : case sensitive 
# age = 10
# Age = 10 
# AGE = 10

# for i in range (1,11):
#     print(i)
# print("hello") # comment

# # comment

# '''multi line comment
# '''

# """_summary_
#     """
# print("Hello ") #  string literal 
# print(10) # integer literal
# print(10.5) # float literal 
# print(True) # boolean literal
# print(False) # boolean literal
# print(None) # None literal
# print([1,2,3,4,5]) # list literal
# print((1,2,3,4,5)) # tuple literal
# print({1,2,3,4,5}) # set literal
# print({1:"one",2:"two",3:"three"}) # dictionary literal
# print(1+2j) # complex literal

# hello = " hello"
# print(hello)


# # string 
# a = "Hello python "
# print(a)
# print(type(a))  #data type of a variable
# print(a[10]) #get element at index 
# print(a[-1]) #get element at last index
# print(a[0:5]) #get element from index m to n-1
# print(a[2:9:2]) #get element from m index to n-1 index with i increments

# print(a+" language") #Concatenate
# b = "programming"
# print(a+b) #Concatenate
# print(a*3) # Repeat the string m times, here 3 times

# c = 42
# print(type(c))
# print(c*3)
# d = str(c)
# print(type(d))
# print(d*3)

# print()
# s = "The python is a programming language"
# print(s)
# l = s.split()
# print(type(l))
# print(l)
# z = "the,python,is,a,programming,language"
# y = z.split(",")
# print(y)

# a = ' '.join(l)
# print(a)
# x = ' '.join(y)
# print(x)

# upper = a.upper()
# print(upper)
# lower = a.lower()   
# print(lower)
# title = a.title()
# print(title)
# txt = "Hello, welcome to my world welcome."
# print(txt)
# x = txt.rfind("welcome")
# print(x)
# b = txt.startswith("Hello")
# print(b)
# c = txt.endswith(" ")
# print(c)
# d = txt.replace("Hello" , "Hi")
# print(d)

# fruit = "   apple   "
# t = fruit.lstrip()
# print("the string after stripping is",t, "the length of the string is ", len(t))
# txt2 = "My name is Ståle"
# uncode = txt2.encode()
# print(uncode)

# x = input("Enter a number: ")
# print(x*3)

# a = 3
# b = 3
# print(a == b)
# print(a is b)

# c = [1,2,3]
# d = [1,2,3]
# print(c == d)   
# print(c is d)

# e = "sadia"
# f = "sadia"
# print(e == f)
# print(e is f)

# g = {1,2,3}
# h = {1,2,3}
# print(g == h)
# print(g is h)

# buildin functions 
# x = max(1,2,3,4,5)
# print(x)

# def sum(a,b): # parameters
#     print(a+b)
# num1 , num2 = 10, 20 
# sum(num1,num2) # arguments

# def text():
#     print("hello")
# text()

# even odd

# defining a function that will check if a number is even or odd
# def even_odd(num):
#     if num % 2 ==0: # condition
#         print("even")
#     else:
#         print("odd")

# # driver code
# a = 4
# even_odd(a)

# default parameter
# def sum(a , b=10 ):
#     print(a+b)

# sum(4)

# # keyword Argument

# def name(first , middle , last):
#     print(first,middle,last)

# name(last="avhad" , first="sadia" , middle="lavesh")
# name(middle = "lavesh", first="sadia", last="avhad")


# positinal argument
# def info(name , age):
#     print("my name is" , name)
#     print("my age is " , age )
# info("sadia" , 20)

# *args and **kwargs
# def info(*args):
#     print(args)

# info(3 ,4 , 5, 6 , 5,7 , 54 , 64, 5, 3)
# info( 34 , "sadia" , [3 ,4, 5] , {45 , 232 , 12} , (1,2,3,4,5))

# def add_numbers(*args):
#     total = sum(args)
#     print("Total:", total)

# add_numbers(10, 20, 30)  


# def info(**kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(f"{key}: {value}")

# info(name="sadia", age=20, city="mumbai")
# info(age = 20, name="sadia", city="mumbai")


# def info():
#     """this is a doc string"""

# print(info.__doc__)

# def info():
#     name = "outer"
#     print(name)
#     def inner():
#         again = "inner"
#         print(again)
    
#     inner()

# info()

# def display(a , b , /):
#     print(a, b)

# display(10 , 20)

# def info( * , a , b):
#     print(a, b)
    
# info(a= 10 , b = 20)

# def combine(a , b , / , * ,  c , d):
#     print(a, b, c, d)

# combine(10 , 20 , c= 50 , d= 80)

# a = lambda : print("hello")
# b = lambda : print(3 +5)
# a()
# b()

# c = lambda name : print("hello" , name)
# b = input("Enter your name: ")
# c(b)

# def func(n):
#     return lambda a : a * n

# multi = func(2)
# print(multi(11))


# a = 10 # global variable 

# def func():
#     a = 20
#     b = a + 2# local variable
#     print(a)
#     print(b)

# func()
# print()

# print(a)
# b = a + 2
# print(b)

# a = "Sadia"
# print(a)

# print(a[0])

# s = """
# this is multi line string
# in python 
# this is how it is done"""

# print(s)

# name = "lavesh"

# print(name[0])
# print(name[-1])

# print(name[::-1])
# print(len(name))
# print(name.upper())
# print(name.lower())

# a = "LAVESH"
# # for i in a:
# #     print(i)

# index = 0
# while index < len(a):
#     print(a[index])
#     index = index + 1


# name = "lavesh"
# age = 20

# print("my name is " + name + "and my age is " + str(age))
# print(f"my name is {name} and my age is {age+56}")

# print("This is the something \"called\" escape sequence")
# print("this is another exampele \"asdsd ")
# print("this is example \\ gfgf")

# txt = "\x47\x75\x72\x75" + "99!"
# print(txt)


# print("hello world", end=" ")
# print("hello world")

# import time

# for i in range(5):
#     print(i, end=" ", flush= True)  # Forces immediate output
#     time.sleep(0.5)  # Pauses for 1 second

# a = b = c = d = 90 #multiple assignment
# print(a, b, c, d) 

# l1 = [1,2,3,4,5]
# a , b ,c , d ,e = l1
# print(l1)
# print(a, b, c, d, e)
# print()
# t1 = (1,2,3,4,5)
# a , b ,c , d ,e = t1
# print(t1)
# print(a, b, c, d, e)

# a , _ , b = 1,2,3
# print(a, b)

# a = 90+10
# print(a)
# b =  "90" + "10"
# print(b)
# c = eval("90+10")
# print(c)

# string formatting
# a = "sadia"
# b = "lavesh" 
# c = 18

# print("my name is {0} and my friend's name is {1} and our age is {2}".format(a, b , c))

# print("{} this is a single place holder". format("lavesh"))
# print(" this is double place holder {}, {} and {}". format("lavesh","sadia", "hehe"))

# Reordering using index
# print("Every {3} should know the use of {2} {1} programming and {0}".format("programmer", "Open", "Source", "Operating Systems"))

# x = None
# print(bool(x)) # false

# x = {}
# print(bool(x)) # false

# x = 0
# print(bool(x))  # false

# x = 1
# print(bool(x))  # true

# x = 67.7
# print(bool(x))  # true

# x = -1
# print(bool(x))  # true

# x = []
# print(bool(x))  # false

# x = "sadia"
# print(bool(x))  # true

# x = range(0, 10)

# for i in x:
#     print(i)
    
# for z in range(0,10):
#     print(z)


