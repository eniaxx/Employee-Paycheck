import menu, commands

class App:

    def __init__(self, start_choice, work_dir):

        self.start_choice = start_choice

        self.work_dir = work_dir

    def start(self):

        print(open('./Menu/welcome.txt').read())

        commands.Database(self.work_dir).initial

        menu.Menu(self.start_choice).command_selection()

App('Start').start()