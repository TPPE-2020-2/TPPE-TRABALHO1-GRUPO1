from errors.errors import OrderError, MissMergeError
from time import sleep
from models.menu import Menu

def main():
    menu = Menu()
    menu.menu()

if __name__ == '__main__':
    main()