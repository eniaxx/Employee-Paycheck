import sqlite3, sys, time, pandas as pd
from tabulate import tabulate

def slowprint(printing_text, speed = 50):
    for c in printing_text + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./speed)

def sqlString(script):

        try:
            c = open('./Scripts/' + script, 'r')
            _script = c.read()
        except ValueError:
            slowprint("\n Can't find script.")
        finally:
            c.close()
        return _script

class MenuApp:

    def selection():   
        print(open(('./Menu/start_menu.txt')).read())

        while True:
            try:
                slowprint('\n Type a number. \n')
                number = int(input())
                break
            except ValueError:
                slowprint('\n Invalid. Use valid number.')

        _selection = 'case_' + str(number)
        getattr(MenuApp, _selection, lambda: \
            (slowprint('\n Incorrect choice. Choose again.'), MenuApp.selection()))()

    def wolfCool(_columns, sqlel):
        with pd.option_context('display.max_columns', None, 'display.max_rows', None):
                df = pd.DataFrame(SqlStatements(sqlString(sqlel)).execute(), \
                columns=_columns)
                df.index = df.index + 1
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    def case_0():
        slowprint('Goodbye.')
        exit()
        
    def case_1():
        _columns = ['Employee ID', 'First Name', 'Last Name', 'Position', 'Birth Date', 'Hire Date'\
                    , 'Salary', 'Bonus', 'Annual Salary', 'Annual Salary and Bonus']
            
        MenuApp.wolfCool(_columns, 'select_all.sql')

    def case_2():
        _columns = ['First Name', 'Last Name', 'Position', \
                    'Annual Salary']
            
        MenuApp.wolfCool(_columns, 'case_2.sql')
        
    def case_3():
        _columns = ['First Name', 'Last Name', 'Position', \
                    'Bonus', 'Annual Salary']
            
        MenuApp.wolfCool(_columns, 'case_3.sql')

    def case_4():
        slowprint(SqlStatements(sqlString('case_4.sql')).simpleQuery('Salary'))

    def case_5():
        slowprint(SqlStatements(sqlString('case_5.sql')).simpleQuery('Annual Salary'))

    def case_6():
        slowprint(SqlStatements(sqlString('case_6.sql')).simpleQuery('Bonus'))

    def case_7():
        slowprint(SqlStatements(sqlString('case_7.sql')).simpleQuery('Bonus and Annual Salary'))

    def case_8():
        _columns = ['First Name', 'Last Name']
            
        MenuApp.wolfCool(_columns, 'case_8.sql')

    def case_9():
        _columns = ['First Name', 'Last Name', 'Position']
            
        MenuApp.wolfCool(_columns, 'case_9.sql')

    def case_10():
        pass
    def case_11():
        pass
    def case_12():
        pass

class SqlStatements:

    def __init__(self, script):
        self.script = script

    def execute(self):

        try:
            con = sqlite3.connect('./Database/EmployeeData.db')
            cur = con.cursor()
            result = cur.execute(self.script).fetchall()        
        except sqlite3.Error as error:
            slowprint('Error occured ' + str(error))
        finally:
            con.close()
        return result

    def simpleQuery(self, case):

        try:
            con = sqlite3.connect('./Database/EmployeeData.db')
            cur = con.cursor()
            result = cur.execute(self.script).fetchone()[0]
        except sqlite3.Error as error:
            return 'Error occurred - ', error
        finally:
            match case:
                case 'Salary':
                    return case + ' Sum is {}'.format(result)
                
                case 'Bonus':
                    return case + ' Sum is {}'.format(result)

                case 'Bonus and Annual Salary':
                    return case + ' Sum is {}'.format(result)

                case 'Annual Salary':
                    return case + ' Sum is {}'.format(result)