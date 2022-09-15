class Main:

    def start():
        from app import MenuApp

        print(open('./Menu/welcome.txt').read() + '\n\n'\
            + open(('./Menu/start_menu.txt')).read())
        
        MenuApp.selection()

Main.start()