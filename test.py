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

# import sqlite3

# con = sqlite3.connect('./Database/EmployeeData.db')
# result = con.cursor(). \
#             execute('select round(sum(Salary),2) from Staff;').fetchone()[0]

# print(result)
# con.close()
# import sqlite3, pandas as pd

# query = sqlite3.connect('./Database/EmployeeData.db')\
# .execute('select MAX(EmployeeID) from Staff;')

# df = pd.DataFrame(data= query.fetchone())[0][0]

# sqlite3.connect('./Database/EmployeeData.db').close()


# print(df)

# print(type(int(df)))

# names = ['David', 'Peter', 50, '2020-10-10', 'Bob']
# for i in range (len (names)):
#     print("{}".format(i + 1, names[i]))

# import names

# for i in range(10):
#     print(names.get_full_name())


# from random import randrange
# from datetime import timedelta

# def random_date(start, end):
#     delta = end - start
#     int_delta = (delta.days * 24 * 60 * 60) # + delta.seconds
#     random_second = randrange(int_delta)
#     return start + timedelta(seconds=random_second)

# from datetime import datetime
# d1 = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
# d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
# print(random_date(d1, d2).strftime('%Y-%m-%d'))

# from tabulate import tabulate

# with pd.option_context('display.max_columns', None, 'display.max_rows', None):
#     con = sqlite3.connect('./Database/EmployeeData.db')
#     query = '''select employeeid,
#                                         firstname,
#                                         lastname,
#                                         title,
#                                         birthdate,
#                                         hiredate,
#                                         salary,
#                                         bonus
#                                 from Staff
#                                 where EmployeeID = 150;'''
    
#     #open('./Scripts/case_2.sql').read()
#     cols = [column[0] for column in con.execute(query).description]
#     df = pd.DataFrame(data= con.execute(query).fetchall(), columns= cols)
#     df.index = df.index + 1
#     print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    
#     print(con.execute(query).fetchone())

#     sqlite3.connect('./Database/EmployeeData.db').close()

#     for i in con.execute(query).description:
#         print(i[0])

#     dx = con.execute(query).fetchone()

#     for i in range(1, len(dx)):
#         print(dx[i])
from calendar import c
import os

script = []

for file in os.scandir('./Scripts'):
    if file.is_file():
        sql_file = open(file, 'r')
        sql_file_content = sql_file.read()
        script.append(sql_file_content)
        
    sql_file.close()

print(script)


match input():
    
    case 'm', 'M':
        pass
    case other:
        pass


    from msilib.schema import Error
from random import randint, randrange
from datetime import timedelta, datetime
from tabulate import tabulate
import sqlite3, sys, os, time, names, pandas as pd

class Application:

    def __init__(self, menu, script_dir):
        
        script = []
        start = []
        con = sqlite3.connect('./Database/EmployeeData.db')

        self.script = script
        self.start = start
        self.con = con

        for file in os.scandir(script_dir):
            if file.is_file():
                sql_file = open(file, 'r')
                sql_file_content = sql_file.read()
                script.append(sql_file_content)
                
            sql_file.close()


        with open(menu) as menu_file:
            for line in menu_file:
                start.append(line)
            menu_file.close()

    @staticmethod
    def slowprint(printing_text, speed = 50):
        for c in printing_text + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./speed)
    
    def selection(self):

        self = self

        while True:
            try:
                print("\n Choose an option.\
                    \n Choose m for printing the menu.\
                    \n Choose c for cleaning the console output.\n")
                key = input()

                match key:

                    case 'm', 'M':
                        

                    if key.lower() == 'm' or key.upper() == 'M':
                        for i in range(0, len(self.start)):
                                print(self.start[i], end= '')
                        continue

                    elif key.lower() == 'c' or key.upper() == 'C':
                        os.system('cls')
                        continue

                finally:

                    if int(key) == 0:
                        self.rightOption(self.start[17])
                        self.slowprint('\n Goodbye. \n')
                        exit()

                    elif int(key) in range(1, 4) or range(8, 15):
                        self.rightOption(self.start[int(key) + 1])

                    elif int(key) in range(4, 8):
                        pass
                    else:
                            print('\n Invalid. Use valid option.')
            
            except ValueError:
                print('\n Incorrect choice. Choose again.')
                continue
            
            finally:
                match int(key):
                    case 1:
                        self.coolTable(index= int(key))
                    case 2:
                        self.coolTable(index= int(key))
                    case 3:
                        self.coolTable(index= int(key))
                    case 4:
                        self.sumQuery(index= int(key), description= 'Monthly Salary')
                    case 5:
                        self.sumQuery(index= int(key), description= 'Annual Salary')
                    case 6:
                        self.sumQuery(index= int(key), description= 'Bonus')
                    case 7:
                        self.sumQuery(index= int(key), description= 'Bonus and Annual Salary')
                    case 8:
                        self.coolTable(index= int(key))
                    case 9:
                        self.coolTable(index= int(key))
                    case 10:
                        self.export(index= 0, x_script= None)
                    case 11:
                        self.export(index= None, x_script= self.sqlOperations('case 11'))
                    case 12:
                        self.sqlOperations('case 12')
                    case 13:
                        self.sqlOperations('case 13')
                    case 14:
                        self.sqlOperations('case 14')

        
            

        # choice = 'case_' + str(key)
        # getattr(self, choice, lambda: (self.slowprint('\n Incorrect choice. Choose again.'), self.selection))()

    def coolTable(self, index):

        with pd.option_context('display.max_columns', None, 'display.max_rows', None):

            query = self.con.execute(self.script[index - 1])

            cols = [column[0] for column in query.description]

            df = pd.DataFrame(data= query.fetchall(), columns= cols)
            df.index = df.index + 1
            
            self.con.close()
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            

    def sumQuery(self, index, description):

        try:
            query = self.con.execute(self.script[index - 1])
            
            df = pd.DataFrame(data= query.fetchone())[0][0]
            self.con.close()
            

        except sqlite3.Error as error:
            return 'Error occurred - ', error

        finally:
            self.slowprint(description + ' Sum is {}'.format(df))

    def rightOption(self, option):

        while True:
            try:
                print('\n Do you wish to continue with:{}?\n'.format(option))
                key = input('\n Y for yes, N for no.\n')

                if key in ['Y', 'y', 'Yes', 'yes']:
                    break
                
                elif key in ['N', 'n', 'No', 'no']:
                    self.selection()
                    
                else:
                    print('\n Invalid. Use valid option.')

            except ValueError:
                print(Error)
                self.selection()

    def export(self, index, x_script):

        if x_script is None:
            execute_script = self.script[index]

        else:
            execute_script = x_script

        try:
            file_name = (str(input('\n Type export file name.\n')) + '.csv')
            
            self.slowprint('\n Executing script......')

            clients = pd.read_sql(execute_script, self.con)
            
            self.slowprint('\n Exporting to {}........'.format(file_name))

            clients.to_csv(file_name, index=False)

            self.slowprint('\n Data exported Successfully into:')
            self.con.close(), print('\n ' + format(os.getcwd()))

        except:
            print(Error)
            self.selection()

    def sqlOperations(self, option):

        table_var = ['First Name', 'Last Name', 'Title or Position', \
                    'Birth Date (Format: 1995-10-15)', 'Hire Date (Format: 2010-10-01)', \
                    'Monthly Salary', 'Bonus']

        match option:
            case 'case 11':
                try:
                    
                    print('\n Type Year (Format: 2022). \n')
                    year = int(input())
                    print('\n Type Month (Format: 01 - 12). \n')
                    month = int(input())
                    print('\n Type Day (Format: 01 - 31). \n')
                    day = int(input())

                    print('\n Do you want to export before or after?\
                    \n 0 - Abort\
                    \n 1 - Before\
                    \n 2 - After \n')
                    x = int(input())
                    match 'Abort' if x == 0 else 'Before' \
                        if x == 1 else 'After' if x == 2 else 'Error':
                        case 'Before':
                            ab = '<='
                        case 'After':
                            ab = '>='
                        case 'Abort':
                            pass
                        case 'Error':
                            pass
                
                except ValueError:
                
                    pass

                finally:

                    return str('''select
                                    *
                                from
	                                staff
                                where
	                                HireDate {} '{}-{}-{} 00:00:00'
                                order by
	                                EmployeeID;''').format(ab, year, month, day)

            case 'case 12':
                try:

                    tx = []

                    query = self.con.execute('select MAX(EmployeeID) from Staff;')

                    df = pd.DataFrame(data= query.fetchone())[0][0]

                    tx.append(df + 1)

                    for i in range(0, 5):

                        print('\n\n Type: ' + table_var[i])
                        tx.append("'" + str(input()) + "'")

                    for i in range(5, 7):
                        print('\n\n Type: ' + table_var[i])
                        tx.append(int(input()))
                    

                    update_query = ('''INSERT OR IGNORE INTO Staff 
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7])

                except ValueError:
                    print(Error)
                    self.selection(self)

                finally:

                    cur = self.con.cursor()
                    cur.execute(update_query)
                    self.con.commit()
                    self.con.close()

                    os.system('cls')

                    self.selection(self)

            case 'case 13':
                try:

                    tx = []

                    con = sqlite3.connect('./Database/EmployeeData.db')
                    query = con\
                            .execute('select MAX(EmployeeID) from Staff;')

                    df = pd.DataFrame(data= query.fetchone())[0][0]

                    tx.append(df + 1)

                    tx.append(names.get_first_name())
                    tx.append(names.get_last_name())

                    d1 = datetime.strptime('1/1/1965 1:30 PM', '%m/%d/%Y %I:%M %p')
                    d2 = datetime.strptime('1/1/2000 0:50 AM', '%m/%d/%Y %I:%M %p')
                    tx.append(self.random_date(d1, d2).strftime('%Y-%m-%d'))

                    d1 = datetime.strptime('1/1/2005 1:30 PM', '%m/%d/%Y %I:%M %p')
                    d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
                    tx.append(self.random_date(d1, d2).strftime('%Y-%m-%d'))

                    tx.append(randint(3000, 11250))
                    tx.append(randint(600, 2125))
                    
                    update_query = ('''INSERT OR IGNORE INTO Staff 
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7])

                except ValueError:
                    print(Error)
                    self.selection()

                finally:

                    cur = con.cursor()
                    cur.execute(update_query)
                    con.commit()
                    con.close()

                    os.system('cls')

                    self.selection()

            case 'case 14':
                try:

                    tx = []

                    con = sqlite3.connect('./Database/EmployeeData.db')

                    print('\n Please type the EmployeeID.\n')
                    tx.append(int(input()))

                    script = ('''select employeeid,
                                        firstname,
                                        lastname,
                                        title,
                                        birthdate,
                                        hiredate,
                                        salary,
                                        bonus
                                from Staff
                                where EmployeeID = {};''').format(tx[0])

                    query = con.execute(script)

                    df = pd.DataFrame(data= query.fetchall(), \
                        columns= [column[0] for column in con.execute(query).description])
                    
                    df.index = df.index + 1

                    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

                    dx = con.execute(query).fetchone()

                    for i in range(1, len(dx)):
                        tx.append(dx[i])


                    
                    update_query = ('''UPDATE Staff
                    
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7])

                except ValueError:
                    print(Error)
                    self.selection()

                finally:

                    cur = con.cursor()
                    cur.execute(update_query)
                    con.commit()
                    con.close()

                    os.system('cls')

                    self.selection()

    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

class SqlStatements:

    def __init__(self, script):
        self.script = script

    def execute(self):

        try:
            con = sqlite3.connect('./Database/EmployeeData.db')
            cur = con.cursor()
            result = cur.execute(self.script).fetchall()        
        except sqlite3.Error as error:
            self.slowprint('Error occured ' + str(error))
        finally:
            con.close()
        return result