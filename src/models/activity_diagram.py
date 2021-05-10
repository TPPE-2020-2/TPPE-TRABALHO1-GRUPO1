from errors.errors import OrderError, MissMergeError
from models.activity_diagram_element import ActivityDiagramElement
from models.transition import Transition
from models.sequence_diagram import SequenceDiagram

class ActivityDiagram():
    def __init__(self, start_node=None, name=''):
        self.elements = {}
        self.transitions = {}
        self.start_node = start_node
        self.name = name
        self.sequence_diagrams = {}

    def __eq__(self, activity_diagram):  # pragma: no cover
        return self.name == activity_diagram.name and \
                self.start_node == activity_diagram.start_node and \
                self.elements == activity_diagram.elements and \
                self.sequence_diagrams == activity_diagram.sequence_diagrams
    
    def __str__(self):  # pragma: no cover
        str_message = r'{' + f'\n\tName: {self.name},\n\tStart Node: {self.start_node},\n\tElements: [\n'
        for element in self.elements.values():
            str_message += '\t\t' + (element.__str__()) + '\n'
        str_message += '\t],\n\tTransitions: [\n'
        for transition in self.transitions.values():
            str_message += '\t\t' + (transition.__str__()) + '\n'
        str_message += '\t],\n\tSequence Diagrams: [\n'
        for sequence_diagram in self.sequence_diagrams.values():
            str_message += '\t\t' + (sequence_diagram.__str__()) + '\n'
        str_message += '\t]\n}'
        return str_message

    def dispose(self):
        self.trasitions = {}
        self.elements = {}
        self.sequence_diagrams = {}
        self.start_node = None
        self.name = ''

    def set_transitions(self, transition):
        self.transitions[transition.name] = transition

    def set_elements(self, element):
        self.elements[element.name] = element
    
    def set_start_node(self, start_node):
        self.start_node = start_node
    
    def set_name(self, name):
        self.name = name

    def set_sequence_diagrams(self, sequence_diagram):
        self.sequence_diagrams[sequence_diagram.get_name()] = sequence_diagram

    def get_name(self):
        return self.name

    def get_elements(self):
        return self.elements

    def get_transitions(self):
        return self.transitions

    def get_start_node(self):
        return self.start_node

    def get_sequence_diagram(self):
        return self.sequence_diagrams

    def activity_diagram_menu(self, name, util, activity_diagram):
        util.clear()
        self.set_name(name)
        sequence_diagram = SequenceDiagram()
        while True:
            print('----- Activity Diagram Menu -----')
            print('Select the element you want to generate:\n'
                f'1 - {util.START_NODE}\n'
                f'2 - {util.ACTIVITY_NODE}\n'
                f'3 - {util.DECISION_NODE}\n'
                f'4 - {util.MERGE_NODE}\n'
                f'5 - {util.END_NODE}\n'
                '6 - Generate Diagram\n'
                '7 - Return to Main Menu')
            user_in = input('Insert your option: ')
            
            if user_in == '1':
                try:
                    util.check_start_node_existence(self.get_elements(), util.START_NODE)
                    start_node_name = input('Insert the Start Node name: ')
                    start_node = ActivityDiagramElement(name=start_node_name, element_type=util.START_NODE)
                    self.set_elements(start_node)
                    self.set_start_node(start_node)
                except OrderError as e:
                    util.print_and_clear(e)
                
            elif user_in == '2':
                try:
                    util.check_start_node_existence(self.get_elements(), util.ACTIVITY_NODE)
                    activity_node_name = input('Insert the Activity Node name: ')
                    activity_node = ActivityDiagramElement(name=activity_node_name, element_type=util.ACTIVITY_NODE)
                    self.set_elements(activity_node)
                    self.add_transition(activity_node, util)
                    print('Create the Sequence Diagram that represents the activity ' + activity_node_name)
                    sequence_diagram = sequence_diagram
                    sequence_diagram = sequence_diagram.sequence_diagram_menu(sequence_diagram, util)
                    self.set_sequence_diagrams(sequence_diagram)
                except OrderError as e:
                    util.print_and_clear(e)

            elif user_in == '3':
                try:
                    util.check_start_node_existence(self.get_elements(), util.DECISION_NODE)
                    decision_node_name = input('Insert the Decision Node name: ')
                    decision_node = ActivityDiagramElement(name=decision_node_name, element_type=util.DECISION_NODE)
                    self.set_elements(decision_node)
                    self.add_transition(decision_node, util)
                except OrderError as e:
                    util.print_and_clear(e)

            elif user_in == '4':
                try:
                    util.check_start_node_existence(self.get_elements(), util.MERGE_NODE)
                    util.check_join_possibility(self.get_elements())
                    merge_node_name = input('Insert the Merge Node name: ')
                    merge_node = ActivityDiagramElement(name=merge_node_name, element_type=util.MERGE_NODE)
                    self.set_elements(merge_node)
                    self.add_transition(merge_node, util)
                except OrderError as e:
                    util.print_and_clear(e)
            
            elif user_in == '5':
                try:
                    util.check_start_node_existence(self.get_elements(), util.END_NODE)
                    util.check_close_possibility(self.get_elements())
                    end_node_name = input('Insert the End Node name: ')
                    end_node = ActivityDiagramElement(name=end_node_name, element_type=util.END_NODE)
                    self.set_elements(end_node)
                    self.add_transition(end_node, util)
                except OrderError as e:
                    util.print_and_clear(e)
                except MissMergeError as e:
                    util.print_and_clear(e)

            elif user_in == '6':
                try:
                    util.generate_diagram(activity_diagram)
                    return 0
                except Exception as e:
                    util.print_and_clear(e)
        
            elif user_in == '7':
                return 0
            
            else:
                util.clear()
                print('Invalid input. Please select again\n')

    def add_transition(self, target_element, util):
        elements = list(self.elements.values())
        position = elements.index(target_element)
        before_element = elements[0:position]
        source = None
        name = input('Type the transition name: ')
        print('Select the source node of the actual node:')
        index = 0
        while True :
            for index, element in enumerate(before_element):
                print(f'{index} - {element}')
            try:
                source = int(input('Type the number of your choice: '))
                if source < 0 or source > index:
                    raise ValueError()
                break
            except ValueError:
                util.print_and_clear(f'You need input a number between 0 and {index}', False)

        while True:
            try:
                prob = float(input('Type the probability of this transition(0.0 - 1.0): '))
                if prob < 0 or prob > 1:
                    raise ValueError()
                break
            except ValueError:
                util.print_and_clear('You need input a number between 0.0 and 1.0', False)

        source_node = self.elements[elements[source].name]

        self.set_transitions(Transition(name=name,
                                        prob=prob,
                                        source=source_node, 
                                        target=target_element, 
                                        element_type=util.TRANSITION_NODE))