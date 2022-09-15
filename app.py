from msilib.schema import Error
import sqlite3, sys, os, time, pandas as pd
from tabulate import tabulate

class MenuApp:

    @staticmethod
    def slowprint(printing_text, speed = 50):
        for c in printing_text + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./speed)
    
    @staticmethod
    def selection():

        M = MenuApp

        with open('./Menu/start_menu.txt') as menu_file:
            lines = []
            for line in menu_file:
                lines.append(line)

            menu_file.close()

        while True:
            try:
                print("\n Choose an option.\
                    \n Choose m for printing the menu.\
                    \n Choose c for cleaning the console output.\n")
                key = input('')

                if key.lower() == 'm' or key.upper() == 'M':
                    print(open(('./Menu/start_menu.txt')).read())

                elif key.lower() == 'c' or key.upper() == 'C':
                    os.system('cls')

                elif int(key) in range(0, 15):

                    if int(key) == 0:
                        MenuApp.rightOption(lines[17])
                        M.slowprint('\n Goodbye. \n')
                        exit()

                    else:

                        MenuApp.rightOption(lines[int(key) + 1])

                    match int(key):

                        case 1:
                            M.coolTable('select_all.sql')

                        case 2:
                            M.coolTable('case_2.sql')

                        case 3:
                            M.coolTable('case_3.sql')

                        case 4:
                            M.sumQuery('case_4.sql', 'Monthly Salary')

                        case 5:
                            M.sumQuery('case_5.sql', 'Annual Salary')

                        case 6:
                            M.sumQuery('case_6.sql', 'Bonus')

                        case 7:
                            M.sumQuery('case_7.sql', 'Bonus and Annual Salary')

                        case 8:
                            M.coolTable('case_8.sql')

                        case 9:
                            M.coolTable('case_9.sql')

                        case 10:
                            M.export('select_all.sql', x_script=None)

                        case 11:
                            M.export(script=None, x_script= M.sqlQuery('case 11'))

                        case 12:
                            M.sqlQuery('case 12')

                        case 13:
                            pass

                        case 14:
                            pass

                else:
                    print('\n Invalid. Use valid option.')
            
            except ValueError:
                print('\n Incorrect choice. Choose again.')
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
            sqlite3.connect('./Database/EmployeeData.db').close()

    @staticmethod
    def sumQuery(script, description):

        try:
            query = sqlite3.connect('./Database/EmployeeData.db').execute(open('./Scripts/' + script).read())
            df = pd.DataFrame(data= query.fetchone())[0][0]
            sqlite3.connect('./Database/EmployeeData.db').close()
            

        except sqlite3.Error as error:
            return 'Error occurred - ', error

        finally:
            MenuApp.slowprint(description + ' Sum is {}'.format(df))

    @staticmethod
    def rightOption(option):

        while True:
            try:
                print('\n Do you wish to continue with:{}?\n'.format(option))
                key = input('\n Y for yes, N for no.\n')

                if key in ['Y', 'y', 'Yes', 'yes']:
                    break
                
                elif key in ['N', 'n', 'No', 'no']:
                    MenuApp.selection()
                    
                else:
                    print('\n Invalid. Use valid option.')

            except ValueError:
                print(Error)
                MenuApp.selection()

    @staticmethod
    def export(script, x_script):

        if x_script is None and script is True:
            execute_script = open('./Scripts/' + script).read()

        else:
            execute_script = x_script

        try:
            file_name = (str(input('\n Type export file name.\n')) + '.csv')
            
            MenuApp.slowprint('\n Executing script......')

            clients = pd.read_sql(execute_script, \
                sqlite3.connect('./Database/EmployeeData.db'))
            
            MenuApp.slowprint('\n Exporting to {}........'.format(file_name))

            clients.to_csv(file_name, index=False)

            MenuApp.slowprint('\n Data exported Successfully into:')
            print('\n ' + format(os.getcwd()))

        except:
            print(Error)
            MenuApp.selection()

    def sqlQuery(option):

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

                table_var = ['First Name', 'Last Name', 'Title or Position', \
                    'Birth Date (Format: 1995-10-15)', 'Hire Date (Format: 2010-10-01)', \
                    'Monthly Salary', 'Bonus']

                tx = []

                try:

                    con = sqlite3.connect('./Database/EmployeeData.db')
                    query = con\
                            .execute('select MAX(EmployeeID) from Staff;')

                    df = pd.DataFrame(data= query.fetchone())[0][0]

                    tx.append(df + 1)

                    for i in range(0, 5):

                        print('\n\n Type: ' + table_var[i])
                        tx.append("'" + str(input()) + "'")

                    for i in range(5, 7):
                        print('\n\n Type: ' + table_var[i])
                        tx.append(int(input()))
                    

                    insert_query = ('''INSERT OR IGNORE INTO Staff 
                    Values({}, {}, {}, {}, {}, {}, {}, {})''')\
                        .format(tx[0], tx[1], tx[2], tx[3], tx[4], tx[5], tx[6], tx[7])

                except ValueError:
                    print(Error)
                    MenuApp.selection()

                finally:

                    cur = con.cursor()
                    cur.execute(insert_query)
                    con.commit()
                    con.close()

                    os.system('cls')

                    MenuApp.selection()

            # params = {
            #     'option': ab,
            #     'date': ("'" + str(year) + '-' + str(month) + '-' + str(day) + "'")
            # }
            
            # from jinja2.utils import markupsafe
            # os.system('python markupsafe.Markup()')
            # os.system('python ')
            # from jinjasql import JinjaSql

            # j = JinjaSql(param_style='pyformat')

            # query, bind_params = j.prepare_query(export_query_template, params)

            # script = str(query % bind_params)

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