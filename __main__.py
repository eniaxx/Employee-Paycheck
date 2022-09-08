class Main:

    def __init__(self, start_choice, work_dir):
        self.start_choice = start_choice

        self.work_dir = work_dir

    def start(self):
        from menu import Menu
        from commands import Database

        print(open('./Menu/welcome.txt').read())

        var = Database(self.work_dir).initial

        Menu(self.start_choice).command_selection()


Main('Start').start()
