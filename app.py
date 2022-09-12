from email.policy import default
import sqlite3, sys, os, time, getpass, pandas as pd
from tabulate import tabulate

class MenuApp(object):

    def __init__(self):
        pass

    @staticmethod
    def slowprint(printing_text, speed = 50):
        for c in printing_text + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./speed)
    
    def selection(self):

        while True:
            try:
                print('\n Type a number to slect option \
                    \n Choose m for printing the menu \
                    \n Choose c for cleaning the console output.')
                key = getpass.getpass('')

                if key == 'm' or key.upper() == 'M':
                    print(open(('./Menu/start_menu.txt')).read())
                    continue

                elif key == 'c' or key.upper() == 'C':
                    os.system('cls')
                    continue

                key = int(key)
                break
            
            except ValueError:
                self.slowprint('\n Invalid. Use valid number.')

        
            choice = 'case_' + str(key)
            default = lambda error: self.slowprint(error) #self.selection(self))
            getattr(self, choice, default('\n Incorrect choice. Choose again.'))(self)

            continue

        # choice = 'case_' + str(key)
        # getattr(self, choice, lambda: (self.slowprint('\n Incorrect choice. Choose again.'), self.selection))()

    @staticmethod
    def coolTable(script):

        with pd.option_context('display.max_columns', None, 'display.max_rows', None):
            query = sqlite3.connect('./Database/EmployeeData.db').execute(open('./Scripts/' + script).read())
            cols = [column[0] for column in query.description]
            df = pd.DataFrame(data= query.fetchall(), columns= cols)
            df.index = df.index + 1
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        # with pd.option_context('display.max_columns', None, 'display.max_rows', None):
        #         df = pd.DataFrame(sqldf(sqlel), \
        #         sqldf(sqlel).columns)
        #         df.index = df.index + 1
        #         print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    def sumQuery(self, script, description):

        try:
            query = sqlite3.connect('./Database/EmployeeData.db').execute(open('./Scripts/' + script).read())
            df = pd.DataFrame(data= query.fetchone())[0][0]
            

        except sqlite3.Error as error:
            return 'Error occurred - ', error

        finally:
            self.slowprint(description + ' Sum is {}'.format(df))

    def case_0(self):

        self.slowprint('\n Goodbye. \n')
        
        exit()
        
    def case_1(self):
            
        self.coolTable('select_all.sql')

        self.selection(self)

    def case_2(self):
            
        self.coolTable('case_2.sql')

        self.selection(self)
        
    def case_3(self):
            
        self.coolTable('case_3.sql')

        self.selection(self)

    def case_4(self):

        self.sumQuery(self, 'case_4.sql', 'Monthly Salary')

        self.selection(self)

    def case_5(self):

        self.sumQuery(self, 'case_5.sql', 'Annual Salary')

        self.selection(self)

    def case_6(self):

        self.sumQuery(self, 'case_6.sql', 'Bonus')

        self.selection(self)

    def case_7(self):

        self.sumQuery(self, 'case_7.sql', 'Bonus and Annual Salary')

        self.selection(self)

    def case_8(self):
            
        self.coolTable('case_8.sql')

        self.selection(self)

    def case_9(self):
            
        self.coolTable('case_9.sql')

        self.selection(self)

    def case_10(self):
        self.selection(self)
        
    def case_11(self):
        self.selection(self)
        
    def case_12(self):
        self.selection(self)

class SqlStatements:

    def __init__(self, script):
        self.script = script

    def execute(self):

        try:
            con = sqlite3.connect('./Database/EmployeeData.db')
            cur = con.cursor()
            result = cur.execute(self.script).fetchall()        
        except sqlite3.Error as error:
            MenuApp.slowprint('Error occured ' + str(error))
        finally:
            con.close()
        return result