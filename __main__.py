class Main:

    def start():
        from app import MenuApp

        print(open('./Menu/welcome.txt').read())
        MenuApp.selection()

Main.start()