# class Shark:
#     def swim(self):
#         print("The shark is swimming.")

#     def be_awesome(self):
#         print("The shark is being awesome.")

# sammy = Shark()
# #sammy.swim()
# #sammy.be_awesome()

# class Python_Switch():
    
#     def switch(self):

#         while True:
#             try:
#                 _switch = int(input('\n Type a number.' + '\n'))
#                 break
#             except ValueError:
#                 print("\n Invalid. Use valid number.")

#         return _switch
    
#     def day(self, month):

#         default = Python_Switch.default_error() #"Incorrect day"

#         return getattr(self, 'case_' + str(month), lambda: default)()
 
#     def default_error():

#         exit()

#     def case_1(self):
#         return "Jan"
 
#     def case_2(self):
#         return "Feb"
 
#     def case_3(self):
#         return "Mar"



# #print(Python_Switch.day(self, 1))
 
# #print(Python_Switch.day(3))

# #my_switch.switch()

# print(Python_Switch.day(Python_Switch.switch(self)))


# class Expando(object):
#     pass

# ex = Expando()
# ex.foo = 17
# ex.bar = "Hello"

# #Expando.fsa =

# Expando.fsx = [1, 2, Expando.fsa]

# print(ex.fsx[2].get('02').get('Salary per Month'))


    # data = []

    # with open('./Database/' + input('\n Type database name. \n') + '.json', 'r') as json_file:
    
    #     database = json.load(json_file)

    # def store(database):



        


#print(type(data[0]))

#print(data[0])


# class Circle(object):

#     pi = 3.14159

#     def __init__(self, radius):

#         self.radius = radius

#     def area(self):
        
#         return Circle.pi * self.radius * self.radius

# print(str(Circle.pi) + '\n')

# #print(str(Circle.__init__(4)) + '\n')

# print(str(Circle(100).area()) + '\n')

# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
 
 
# iterate all the nested dictionaries with keys

  # display
#print(sum(d[data[i].get('Age') for i in data]) for d in data[i])
    
    
    #print(data[i].values())



# import os
# import sys

# items = os.listdir("./Menu")

# fileList = [name for name in items if name.endswith(".txt")]

# for cnt, fileName in enumerate(fileList, 1):
#     sys.stdout.write("[%d] %s\n\r" % (cnt, fileName))

# choice = int(input("Select txt file[1-%s]: " % cnt)) - 1
# print(fileList[choice])

# print(str(fileList[choice]))

# print('hurrraaa')


# from time import sleep

# def print_slow(txt):
#     for x in txt:                     # cycle through the text one character at a time
#         print(x, end='', flush=True)  # print one character, no new line, flush buffer
#         sleep(0.04)
#     print() # go to new line

# print_slow("Hello. I'm feeling a bit slow today")


# import sys
# import time
# def slowprint(s):
# 	for c in s + '\n':
# 		sys.stdout.write(c)
# 		sys.stdout.flush()
# 		time.sleep(1./10)
# slowprint("this this writen slowly in my terminal")

import sqlite3

con = sqlite3.connect('./Database/EmployeeData.db')
result = con.cursor(). \
            execute('select round(sum(Salary),2) from Staff;').fetchone()[0]

print(result)
con.close()