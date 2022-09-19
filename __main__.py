class Main:

    def start():
        from app import Application

        print(open('./Menu/welcome.txt').read() + '\n\n'\
            + open(('./Menu/start_menu.txt')).read())
        
        Application.selection()

Main.start()