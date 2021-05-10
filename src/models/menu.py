from models.lifeline import Lifeline
from models.message import Message
from models.activity_diagram import ActivityDiagram
from utils.utils import Util
from time import sleep

util = Util()

class Menu:
    def __init__(self):
        pass
    
    def menu(self):
        activity_diagram = ActivityDiagram()
        while True:
            print('----- Main Menu -----')
            print('Select the diagram you want to generate:\n'
                '1 - Activity Diagram\n'
                '2 - Exit')
            user_in = input('Insert your option: ')
            
            if user_in == '1':
                print('----- Activity Diagram -----')
                name = input('Insert the Activity Diagram name: ')
                activity_diagram.activity_diagram_menu(name, util, activity_diagram)
                sleep(5)
                util.clear()
            elif user_in == '2':
                print('Leaving the program!')
                return 0
            else:
                util.clear()
                print('Invalid input. Please select again\n')