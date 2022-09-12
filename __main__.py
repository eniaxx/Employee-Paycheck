from app import MenuApp


class Main:

    def start():
        from app import MenuApp

        print(open('./Menu/welcome.txt').read())
        print(open(('./Menu/start_menu.txt')).read())
        MenuApp.selection(self=MenuApp)

Main.start()