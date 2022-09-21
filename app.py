from msilib.schema import Error
from tabulate import tabulate
from datetime import datetime
import sqlite3, sys, os, time, names, re, random, pandas as pd

class Application:

    def __init__(self, menu, script_dir):
        
        script = []
        start = []
        con = sqlite3.connect('./Database/EmployeeData.db')
        description = ['Monthly Salary', 'Annual Salary', 'Bonus', 'Bonus and Annual Salary']

        self.script = script
        self.start = start
        self.con = con
        self.description = description

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

    def selection(self):

        while True:
            try:
                print("\n Choose an option.\
                    \n Choose m for printing the menu.\
                    \n Choose c for cleaning the console output.\n")
                key = input()

                match key:

                    case 'm' | 'M':
                        for i in range(0, len(self.start)): print(self.start[i], end= '')

                    case 'c' | 'C':
                        os.system('cls')

                    case '0':
                        self.rightOption(self.start[-1])
                        self.slowprint('\n Goodbye. \n')
                        self.con.close()
                        exit()

                    case '1' | '2' | '3' | '8' | '9':
                        self.coolTable(index= int(key))

                    case '4' | '5' | '6' | '7':
                        self.sumQuery(index= int(key), description= self.description[int(key) - 4])

                    case '10':
                        self.rightOption(self.start[int(key) + 1])
                        self.export(key)

                    case '11':
                        self.rightOption(self.start[int(key) + 1])
                        self.export(key)

                    case '12' | '13' | '14' | '15':
                        self.rightOption(self.start[int(key) + 1])
                        self.sqlOperations(option= key)

                    case _:
                            print('\n Invalid. Use valid option.')
            
            except ValueError:
                print('\n Incorrect choice. Choose again.')
                continue
    
    def coolTable(self, index):

        with pd.option_context('display.max_columns', None, 'display.max_rows', None):

            query = self.con.execute(self.script[index - 1])
            cols = [column[0] for column in query.description]

            df = pd.DataFrame(data= query.fetchall(), columns= cols)
            df.index = df.index + 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            

    def sumQuery(self, index, description):

        try:
            query = self.con.execute(self.script[index - 1])
            df = pd.DataFrame(data= query.fetchone())[0][0]

        except sqlite3.Error as error:
            return 'Error occurred - ', error

        finally:
            self.slowprint(description + ' Sum is {}'.format(df))

    def export(self, key):

        match key:

            case '10': script = self.script[0]

            case '11':
                    while True:
                        try:
                            year = input('\n Type Year (Format: 2022). \n')

                            if re.match('^[0-9]{4}$', year):
                                pass
                            else:
                                print('\n Invalid. Use valid option.')
                                continue

                            month = input('\n Type Month (Format: 01 - 12). \n')

                            if 12 >= int(month) >= 1:
                                pass
                            else:
                                print('\n Invalid. Use valid option.')
                                continue

                            day = input('\n Type Day (Format: 01 - 31). \n')

                            if  12 >= int(day) >= 1:
                                pass
                            else:
                                print('\n Invalid. Use valid option.')
                                continue

                            decision = input('\n Do you want to export before or after?\
                            \n 0 - Abort\
                            \n 1 - Before\
                            \n 2 - After \n')

                            match decision:
                                case '1' | 'Before':
                                    decision = '<='
                                case '2' | 'After':
                                    decision = '>='
                                case '0' | 'Abort':
                                    self.selection()
                                case _:
                                    print(Error)
                                    self.selection()


                            script = str(('''select
                                        *
                                    from
	                                    staff
                                    where
	                                    HireDate {} '{}-{}-{} 00:00:00'
                                    order by
	                                    EmployeeID;''').format(decision, year, month, day))

                            break

                        except ValueError:
                            print(Error)
                            self.selection()

        try:
            file_name = (str(input('\n Type export file name.\n')) + '.csv')
            
            self.slowprint('\n Executing script......')

            clients = pd.read_sql(script, self.con)
            
            self.slowprint('\n Exporting to {}........'.format(file_name))

            clients.to_csv(file_name, index=False)

            self.slowprint('\n Data exported Successfully into:')
            print('\n ' + format(os.getcwd()))

        except:
            print(Error)
            self.selection()

    def sqlOperations(self, option):

        table_var = ['First Name', 'Last Name', 'Title or Position', \
                    'Birth Date (Format: 1995-10-15)', 'Hire Date (Format: 2010-10-01)', \
                    'Monthly Salary', 'Bonus']

        match option:

            case '12':
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
                    

                    update_query = str(('''INSERT OR IGNORE INTO Staff 
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7]))

                except ValueError:
                    print(Error)
                    self.selection()

            case '13':
                try:

                    tx = []
                    query = self.con.execute('select MAX(EmployeeID) from Staff;')

                    df = pd.DataFrame(data= query.fetchone())[0][0]

                    tx.append(df + 1)

                    tx.append(names.get_first_name())
                    tx.append(names.get_last_name())

                    tx.append(random.choice(open('./Database/tittle_list.txt').read().splitlines()))

                    d1 = datetime.strptime('1/1/1965 1:30 PM', '%m/%d/%Y %I:%M %p')
                    d2 = datetime.strptime('1/1/2000 0:50 AM', '%m/%d/%Y %I:%M %p')
                    tx.append(datetime.strftime(self.random_date(d1, d2), '%Y-%m-%d'))

                    d1 = datetime.strptime('1/1/2005 1:30 PM', '%m/%d/%Y %I:%M %p')
                    d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
                    tx.append(datetime.strftime(self.random_date(d1, d2), '%Y-%m-%d'))
                    
                    #tx.append(self.random_date(d1, d2).strftime('%Y-%m-%d'))

                    tx.append(random.randint(3000, 11250))
                    tx.append(random.randint(600, 2125))
                    
                    update_query = str(('''INSERT OR IGNORE INTO Staff 
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7]))

                except ValueError:
                    print(Error)
                    self.selection()

            case '14':
                try:

                    tx = []
                    
                    tx.append(int(input('\n Please type the EmployeeID.\n')))

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

                    query = self.con.execute(script)

                    df = pd.DataFrame(data= query.fetchall(), \
                        columns= [column[0] for column in query.description])
                    
                    df.index = df.index + 1

                    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

                    while True:

                        x = input('\n Do you want to abort?\
                            \n Yes - y\
                            \n No  - n\n')

                        match x:
                            case 'Yes' | 'yes' | 'Y' | 'y':
                                break

                            case 'No' | 'no' | 'N' | 'n':
                                self.selection()

                            case _:
                                print('\n Type again.')
                                continue

                    for i in range(0, 5):

                        print('\n\n Type: ' + table_var[i])
                        tx.append("'" + str(input()) + "'")

                    for i in range(5, 7):

                        print('\n\n Type: ' + table_var[i])
                        tx.append(int(input()))
                    
                    update_query = ('''UPDATE Staff
                    
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7])

                except ValueError:
                    print(Error)
                    self.selection()
        
            case '15':

                idx = (int(input('\n Please type the EmployeeID.\n')))

                update_query = str(('DELETE FROM Staff WHERE EmployeeID={};').format(idx))

            case _:
                print('Error')
                self.selection()


        cur = self.con.cursor()
        cur.execute(update_query)
        self.con.commit()

        self.slowprint('\n Executing ' + self.start[int(option) + 1])

        self.selection()

    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + timedelta(seconds=random_second)