from models.user_in import UserIn
from models.fragment import Fragment
class FragmentIn(UserIn):
    def __init__(self):
        self.fragments = []
    def add(self, info):
        fragment_name = input('Insert the Fragment name: ')
        if info != None:
            diagram_name = info
            sequence_diagram = None
        else:
            diagram_name = input('Insert the Sequence Diagram name: ')
            print('Create the Sequence Diagram that is represented by the fragment ' + fragment_name)
            sequence_diagram = create_sequence_diagram(diagram_name)
            sequence_diagram.set_fragments(Fragment(name=fragment_name, represented_by=diagram_name))
            sequence_diagram = sequence_diagram_menu(sequence_diagram)
        fragment = Fragment(name=fragment_name, represented_by=diagram_name, sequence_diagram=sequence_diagram)
        self.fragments.append(fragment)