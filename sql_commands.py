import sqlite3, pandas as pd, numpy as np
from tabulate import tabulate
import commands

printing = commands.slowprint


class ExecuteSQL:

    def __init__(self, script):
        self.script = script
        self.connection = sqlite3.connect('./Database/EmployeeData.db')
        self.sql_folder = './Scripts'

    @staticmethod
    def create_sql_string(sql_file):

        # Open the external sql file.
        file = open(sql_file, 'r')

        # Read out the sql script text in the file.
        sql_script_string = file.read()

        # Close the sql file object.
        file.close()

        # Execute the read-out sql script string.
        return sql_script_string

    def establish_connection(self):

        try:
            var = self.connection
            return 'Connection established.'
        except self.connection.Error as error:
            return 'Error occurred while connecting - ', error

    def query(self):

        try:

            result = ExecuteSQL.connection.cursor(). \
                execute(self.script).fetchall()

            return result

        except sqlite3.Error as error:

            return 'Error occurred - ', error

    def total(self, case):

        match case:

            case 'Salary':
                file = '/sum_Salary.sql'

            case 'Bonus':
                file = '/sum_Bonus.sql'

        script = ExecuteSQL.create_sql_string(self.sql_folder + file)

        try:

            result = self.connection.cursor(). \
                execute(script).fetchall()[0][0]

            return case + ' Sum is {}'.format(result)

        except sqlite3.Error as error:

            return 'Error occurred - ', error


database = './Database/EmployeeData.db'
query = 'select firstName, lastName, title from staff;'

printing(establish_connection())

printing(total('Bonus'))

printing(total('Salary'))

printing(total('Bonus') + total('Salary'))

with pd.option_context('display.max_columns', None, 'display.max_rows', None):
    df = pd.DataFrame(ExecuteSQL(query).query(), columns=['First Name', 'Last Name', 'Position'])

    df.index = df.index + 1

    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
