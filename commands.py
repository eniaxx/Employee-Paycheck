import os, sys, json, pandas, time
import menu

class Database:

    def __init__(self, work_dir):
        
        self.work_dir = work_dir


    def load(self):

        fileList = [name for name in self.work_dir if name.endswith('.json')]

        for count, fileName in enumerate(fileList, 1):
            sys.stdout.write("[%d] %s\n\r" % (count, fileName))

        choice = int(input("Select txt file[1-%s]: " % count)) - 1
        
        print(fileList[choice])

        with open(fileList[choice], 'r') as file:

            Operation.store(str(fileList[choice]), file)

        Operation.store

        print(fileList[choice])
        


    def list_Database(self):

        print(pandas.DataFrame(data = os.listdir(self.work_dir)))

    def database_name():

        Database.list_Database()

        json_file = input('\n Type database name. \n')

        return json_file

    def read(name):
        
         # Opening JSON file
        with open('./Database/' + name + '.json', 'r') as _name:

        # Reading from json file
            database = json.load(_name)
    
        return database

    def write(database):
 
        # Serializing json
        json_file = json.dumps(database, indent=4)
 
        # Writing to .json
        with open('./Database/' + input('\n Type name.json. \n'), 'w') as outfile:
    
            outfile.write(json_file)

    def print(database):

        print(pandas.DataFrame(database))

class Operation:

    l_d = [] #cached data database

    l_n = [] #cached data name

    menu_case = "" #Menu variable, currently Start and Employee

    #temp_dictionary = {} #temporary place for dictionaries / databases

    def store(name, database):
        
        Operation.l_n.append(name)

        Operation.l_d.append(database)

    def clear():

        Operation.l_d.clear()

        Operation.l_n.clear()

    def empty_database_check():

        if (Operation.quantity() == 1):

            pass

        elif (Operation.quantity() >= 2):

            pass

        else:

            print("\n Invalid. You didn't load a database.")

            menu.Menu.init_menu(Operation.menu_case)
    
    def print_loaded_databases_names():

        if Operation.empty_database_check() is True:

            print("Loaded Databases: \n")

            print(*Operation.l_n, sep = "\n")
        
        else:

            print(" Something went wrong. \n Suggestion: Try again or Close the programm.")

            #start something
        
            #print(pandas.DataFrame(data = Operation.l_n[0]))

    def quantity():

        return len(Operation.l_d)

    def sum(choice):

        if (Operation.quantity() == 1):

            return sum(item[choice] for item in Operation.l_d[0])

        elif (Operation.quantity() >= 2):

            for i in Operation.l_d:

                return sum(item[choice] for item in Operation.l_d[i])

        else:

            pass

 
@staticmethod
def slowprint(printing_text):

    for c in printing_text + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)