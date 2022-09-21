class Main:

    def start():
        from app import Application

        welcome = open('./Menu/welcome.txt')
        menu = './Menu/start_menu.txt'
        start = open(menu)

        print(welcome.read() + '\n\n' + start.read())

        welcome.close(), start.close()
        
        Application(menu= menu, script_dir= './Scripts/').selection()

Main.start()