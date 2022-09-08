import sqlite3, pandas as pd, numpy as np
from tabulate import tabulate
import commands

printing = commands.slowprint

class sql:

    database = './Database/EmployeeData.db'
    sql_folder = './Scripts'
    connection = sqlite3.connect(database)

    def __init__(self, script):

        self.script = script

    @staticmethod
    def establish_connection():

        try:
            sql.connection

            return ('Connection established.')

        except sql.connection.Error as error:
            
            return ('Error occured while connecting - ', error)

    @staticmethod
    def close_connection():

        try:
            sql.connection.close()

            return ('Closing connection without errors.')

        except:
            
            return ('Error occured while closing - ')

    @staticmethod
    def create_sql_string(sql_file):

    # Open the external sql file.
        file = open(sql_file, 'r')
    
    # Read out the sql script text in the file.
        sql_script_string = file.read()
    
    # Close the sql file object.
        file.close()
    
    # Execute the read out sql script string.
        return sql_script_string


    @staticmethod
    def sum(case):

        match case:

            case 'Salary':
                file = '\sum_Salary.sql'

            case 'Bonus':
                file = '\sum_Bonus.sql'

        query = sql.create_sql_string(sql.sql_folder + file)

        try:

            result = sql.connection.cursor().\
                execute(query).fetchall()[0][0]

            return (case + ' Sum is {}'.format(result))


        except sqlite3.Error as error:
            
            return ('Error occured - ', error)

    def query(self):

        try:

            result = sql.connection.cursor().\
                execute(self.script).fetchall()

            return result

        except sqlite3.Error as error:
            
            return ('Error occured - ', error)


database = '.\Database\EmployeeData.db'
query = 'select firstName, lastName, title from staff;'

printing(sql.establish_connection())

printing(sql.sum('Bonus'))

printing(sql.sum('Salary'))

with pd.option_context('display.max_columns', None, 'display.max_rows', None):

    df = pd.DataFrame(sql(query).query(), columns=['First Name', 'Last Name', 'Position'])

    df.index = df.index + 1

    print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid'))

printing(sql.close_connection())