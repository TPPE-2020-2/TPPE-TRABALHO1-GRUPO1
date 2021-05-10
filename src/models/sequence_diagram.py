from models.sequence_diagram_element import SequenceDiagramElement
from models.lifeline import Lifeline
from models.fragment import Fragment
from models.message import Message

class SequenceDiagram():
    def __init__(self, name='', guard_condition=''):
        self.name = name
        self.guard_condition = guard_condition
        self.life_lines = {}
        self.messages = {}
        self.fragments = []

    def __eq__(self, sequence_diagram):  # pragma: no cover
        return self.name == sequence_diagram.name and \
            self.guard_condition == sequence_diagram.guard_condition and \
            self.life_lines == sequence_diagram.life_lines and \
            self.messages == sequence_diagram.messages and \
            self.fragments == sequence_diagram.fragments
    
    def __str__(self):  # pragma: no cover
        return 'Name: {}\nGuard Condition: {}\nLife Lines: {}\nElements: {}\n'.format(self.name, \
                                                                            self.guard_condition, \
                                                                            self.life_lines, \
                                                                            self.messages, \
                                                                            self.fragments)

    def dispose(self):
        self.name = ''
        self.guard_condition = ''
        self.life_lines = {}
        self.messages = {}
        self.fragments = []

    def set_name(self, name):
        self.name = name
   
    def set_guard_condition(self, guard_condition):
        self.guard_condition = guard_condition
    
    def set_life_lines(self, life_lines: dict):
        self.life_lines = life_lines
  
    def set_messages(self, messages):
        self.messages[messages.get_name()] = messages

    def set_fragments(self, fragments):
        self.fragments.append(fragments)

    def get_name(self):
        return self.name
   
    def get_guard_condition(self):
        return self.guard_condition

    def get_life_lines(self):
        return self.life_lines
  
    def get_messages(self):
        return self.messages

    def get_fragments(self):
        return self.fragments

    def create_sequence_diagram(self, diagram_name=None):
        print('----- Sequence Diagram -----')
        if diagram_name != None:
            self.name = diagram_name
        else:
            name = input('Insert the Sequence Diagram name: ')
        print('Insert the guard condition:',
                                '\n1 - True',
                                '\n2 - False')
        guard_condition = input()
        guard_condition = True if guard_condition == 1 else False
        sequence_diagram = SequenceDiagram(name=name, guard_condition=guard_condition)
        return sequence_diagram

    def sequence_diagram_menu(self, sequence_diagram, util):
        util.clear()
        lifeline = Lifeline()
        message = Message()
        lifelines = lifeline.get_lifelines()
        self.set_life_lines(lifelines)
        while True:
            print('----- Sequence Diagram Menu -----')
            print('Select the element you want to generate:\n'
                f'1 - {util.MESSAGE}\n'
                f'2 - {util.FRAGMENT}\n'
                '3 - Return to Activity Diagram Menu')
            user_in = input('Insert your option: ')
            if user_in == '1':
                self.set_messages(message.add_message(lifelines))
            elif user_in == '2':
                if len(self.fragments) == 0:
                    self.set_fragments(self.add_fragment(self.name))
                else:
                    self.set_fragments(self.add_fragment())
            elif user_in == '3':
                self.fragments[0].sequence_diagram = sequence_diagram
                return sequence_diagram
            else:
                util.clear()
                print('Invalid input. Please select again\n')

    def add_fragment(self, sequence_diagram_name=None):
        fragment_name = input('Insert the Fragment name: ')
        if sequence_diagram_name != None:
            diagram_name = sequence_diagram_name
            sequence_diagram = None
        else:
            diagram_name = input('Insert the Sequence Diagram name: ')
            print('Create the Sequence Diagram that is represented by the fragment ' + fragment_name)
            sequence_diagram = self.create_sequence_diagram(diagram_name)
            self.set_fragments(Fragment(name=fragment_name, represented_by=diagram_name))
            sequence_diagram = self.sequence_diagram_menu(sequence_diagram)
        fragment = Fragment(name=fragment_name, represented_by=diagram_name, sequence_diagram=sequence_diagram)
        return fragment