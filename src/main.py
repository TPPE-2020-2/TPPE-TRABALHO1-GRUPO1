from models.activity_diagram import ActivityDiagram
from models.activity_diagram import ActivityDiagram
from models.sequence_diagram import SequenceDiagram
from models.fragment import Fragment
from models.activity_diagram_element import ActivityDiagramElement
from models.transition import Transition
from models.lifeline import Lifeline
from models.message import Message
from models.message_in import MessageIn
from models.fragment_in import FragmentIn
from errors.errors import OrderError, MissMergeError
from utils.utils import Util
from time import sleep

util = Util()


def main():
    while(True):
        print('----- Main Menu -----')
        print('Select the diagram you want to generate:\n'
            '1 - Activity Diagram\n'
            '2 - Exit')
        user_in = input('Insert your option: ')
        
        if(user_in == '1'):
            print('----- Activity Diagram -----')
            name = input('Insert the Activity Diagram name: ')
            activity_diagram_menu(name)
            sleep(5)
            util.clear()
        # elif(user_in == '2'):
        #     print('----- Sequence Diagram -----')
        #     name = input('Insert the Sequence Diagram name: ')
        #     print('Insert the guard condition:',
        #                             '\n 1 - True',
        #                             '\n 2 - False')
        #     guard_condition = input()
        #     guard_condition = True if guard_condition == 1 else False
        #     sequence_diagram = SequenceDiagram(name=name, guard_condition=guard_condition)
        #     sequence_diagram_menu(sequence_diagram)
        #     util.clear()
        elif(user_in == '2'):
            print('Leaving the program!')
            return 0
        else:
            util.clear()
            print('Invalid input. Please select again\n')


def activity_diagram_menu(name):
    util.clear()
    activity_diagram = ActivityDiagram(name=name)
    while(True):
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
                util.check_start_node_existence(activity_diagram.get_elements(), util.START_NODE)
                start_node_name = input('Insert the Start Node name: ')
                start_node = ActivityDiagramElement(name=start_node_name, element_type=util.START_NODE)
                activity_diagram.set_elements(start_node)
                activity_diagram.set_start_node(start_node)
            except OrderError as e:
                util.print_and_clear(e)
            
        elif user_in == '2':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.ACTIVITY_NODE)
                activity_node_name = input('Insert the Activity Node name: ')
                activity_node = ActivityDiagramElement(name=activity_node_name, element_type=util.ACTIVITY_NODE)
                activity_diagram.set_elements(activity_node)
                add_transition(activity_diagram, activity_node)
                print('Create the Sequence Diagram that represents the activity ' + activity_node_name)
                sequence_diagram = create_sequence_diagram()
                sequence_diagram = sequence_diagram_menu(sequence_diagram)
                activity_diagram.set_sequence_diagrams(sequence_diagram)
            except OrderError as e:
                util.print_and_clear(e)

        elif user_in == '3':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.DECISION_NODE)
                decision_node_name = input('Insert the Decision Node name: ')
                decision_node = ActivityDiagramElement(name=decision_node_name, element_type=util.DECISION_NODE)
                activity_diagram.set_elements(decision_node)
                add_transition(activity_diagram, decision_node)
            except OrderError as e:
                util.print_and_clear(e)

        elif user_in == '4':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.MERGE_NODE)
                util.check_join_possibility(activity_diagram.get_elements())
                merge_node_name = input('Insert the Merge Node name: ')
                merge_node = ActivityDiagramElement(name=merge_node_name, element_type=util.MERGE_NODE)
                activity_diagram.set_elements(merge_node)
                add_transition(activity_diagram, merge_node)
            except OrderError as e:
                util.print_and_clear(e)
           
        elif user_in == '5':
            try:
                util.check_start_node_existence(activity_diagram.get_elements(), util.END_NODE)
                util.check_close_possibility(activity_diagram.get_elements())
                end_node_name = input('Insert the End Node name: ')
                end_node = ActivityDiagramElement(name=end_node_name, element_type=util.END_NODE)
                activity_diagram.set_elements(end_node)
                add_transition(activity_diagram, end_node)
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


def sequence_diagram_menu(sequence_diagram):
    util.clear()
    lifelines = get_lifelines()
    sequence_diagram.set_life_lines(lifelines)
    items = [MessageIn(), FragmentIn()]
    info = [lifelines, sequence_diagram.name]
    while True:
        print('----- Sequence Diagram Menu -----')
        print('Select the element you want to generate:\n'
              f'1 - {util.MESSAGE}\n'
              f'2 - {util.FRAGMENT}\n'
              '3 - Return to Activity Diagram Menu')
        user_in = input('Insert your option: ')
        if user_in == '1' or user_in == '2':
            option = int(user_in)-1
            items[option].add(info[option])
        elif user_in == '3':
            sequence_diagram.set_messages(items[0].messages)
            sequence_diagram.set_fragments(items[1].fragments)
            sequence_diagram.fragments[0].sequence_diagram = sequence_diagram
            return sequence_diagram
        else:
            util.clear()
            print('Invalid input. Please select again\n')


def add_transition(activity_diagram, target_element):
    elements = list(activity_diagram.elements.values())
    position = elements.index(target_element)
    before_element = elements[0 : position]
    source = None
    name = input('Type the transition name: ')
    print('Select the source node of the actual node:')
    index = 0
    while(True):
        for index, element in  enumerate(before_element):
            print(f'{index} - {element}')
        try:
            source = int(input('Type the number of your choice: '))
            if(source<0 or source>index):
                raise ValueError()
            break
        except ValueError:
            util.print_and_clear(f'You need input a number between 0 and {index}', False)

    while(True):
        try:
            prob = float(input('Type the probability of this transition(0.0 - 1.0): '))
            if(prob<0 or prob>1):
                raise ValueError()
            break
        except ValueError:
            util.print_and_clear('You need input a number between 0.0 and 1.0', False)

    source_node = activity_diagram.elements[elements[source].name]

    activity_diagram.set_transitions(Transition(name=name,
                                                prob=prob,
                                                source=source_node, 
                                                target=target_element, 
                                                element_type=util.TRANSITION_NODE))


def get_lifelines():
    lifelines = {}
    lifelines_amount = input('Insert the number of lifelines:')
    for index, lifeline in enumerate(range(int(lifelines_amount))):
        print(f'Insert the {index + 1} Lifeline name: ')
        lifeline_name = input()
        lifeline = Lifeline(id=index, name=lifeline_name)
        lifelines[index] = lifeline
        print()
    return lifelines

def create_sequence_diagram(diagram_name=None):
    print('----- Sequence Diagram -----')
    if diagram_name != None:
        name = diagram_name
    else:
        name = input('Insert the Sequence Diagram name: ')
    print('Insert the guard condition:',
                            '\n 1 - True',
                            '\n 2 - False')
    guard_condition = input()
    guard_condition = True if guard_condition == 1 else False
    sequence_diagram = SequenceDiagram(name=name, guard_condition=guard_condition)
    return sequence_diagram

if __name__ == '__main__':
    main()