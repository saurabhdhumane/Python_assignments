""" 
1 Day - 13 Dec 2021 
Name : Saurabh Dhumane

"""

#Basic Sytax Of Python

#This is Single line Comments......

"""
        This Is Multiple Line 
            Comments Statements

"""

#Print Statements In Python

print("Hello World")

print("2+3")
print(2+3)

a= 21+3
b = 234
print(a+b)

introduction = "Welcome To Stupid School"
print(introduction)

print("Hello "+introduction)
print("Hello "+introduction)
print("Hello"+""+introduction)
print("hello Students {}".format(introduction))

Name = "Raje"
plateform = 'Student Hub'
language = "Python"
Date = "13 December 2021"
total = 500


#format in print example
print(" My Name Is {}".format(Name))

print("My Name Is {} And I Using {} Programing".format(Name,language))

print("My Name Is {} And I Using {} Programing language At {} and The Date On {}".format(Name,language,plateform,Date))
print("My Name Is {0} And I Using {1} Programing language At {2} and The Date On {3}".format(Name,language,plateform,Date))
print("My Name Is {3} And I Using {2} Programing language At {1} and The Date On {0}".format(Name,language,plateform,Date))
print("2 + 3 = {}".format(2+3))
print("2 + 3 = {}".format(str(2+3)))

#data types print example
print("Hello My Name Is %s"%(Name))
print("Hello My Name Is %s And I Learn %s at %s on %s"%(Name,language,plateform,Date))

print("Hello My Name Is %s And I Learn %s at %s on %s the total is %s"%(Name,language,plateform,Date,total))
print("Hello My Name Is %s And I Learn %s at %s on %s the total is %f"%(Name,language,plateform,Date,total))
print("Hello My Name Is %s And I Learn %s at %s on %s the total is %d"%(Name,language,plateform,Date,total))
print("77+3 is =%d"%(77+3))

#ftype print

print(f"name is {Name}")
print(f"name is {Name} and i love to lern {language} at{plateform} on{Date} and the total count is {total}")
print(f"23+45 = {23+45}")
print(f'23+45 = {23+45}')
print(f"my name is {'Raje'}")
print(f'my name is {"Raje"}')

print(f"Which is Greter ::{12<4}")
print(f"Which is Greter ::{12>4}")


"""


Data Types In Python


"""
#int
num = 213
arg = 45

print(arg)
print(num)
print(type(num))
print(type(arg))

#float

marks = 32.43
income = 32.545

print(marks)
print(income)

print(type(marks))
print(type(income))


# String

string = "Hello World"

travel = 'goa'

print(string)
print(travel)

print(type(string))
print(type(travel))

#boolean  
isGreater = True
isLesser = False

print(isGreater)
print(isLesser)

print(type(isGreater))
print(type(isLesser))



#List (List Or Array) - collection of items
fruits = ["Apple", "banana", "Mango", "Cherry", "Orange"] 
print(fruits)
print(type(fruits))

boolen_List = [True, False, True, False]
print(boolen_List)

mix_list = [12.12 , 12, "banana", 'hello', True, False]
print(mix_list)

#append property or add a item in list (insert append elements in left)

mix_list.append('Raje')
print(mix_list)

mix_list.insert(0,'Stupid School')

print(mix_list)

mix_list.insert(3,'Student Hub')
print(mix_list)

mix_list.insert(4,"Student Hub")
print(mix_list)

mix_list.append("12.12")
print(mix_list)
print(mix_list.count('Student Hub'))

print(mix_list.count('Hub'))


for each in mix_list:
   # print(each)
   
    if type(each)==str:
        print(each)





