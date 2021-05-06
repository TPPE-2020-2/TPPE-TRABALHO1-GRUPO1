from utils.utils import Util
util = Util()


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

    def to_xml(self):
        xml = f'<ActivityDiagram name="{self.name}">\n'
        xml += util.get_tab(4) + '<ActivityDiagramElements>\n'
        for element in self.elements.values():
            xml += util.get_tab(8) + element.to_xml() + '\n'
        xml += util.get_tab(4) + '</ActivityDiagramElements>\n'
        xml += util.get_tab(4) + '<ActivityDiagramTransitions>\n'
        for transition in self.transitions.values():
            xml += util.get_tab(8) + transition.to_xml() + '\n'
        xml += util.get_tab(4) + '</ActivityDiagramTransitions>\n'
        xml += '</ActivityDiagram>\n'
        for sequence_diagram in self.sequence_diagrams.values():
            print('Act Dg sq: ' + str(type(sequence_diagram)))
            xml += sequence_diagram.to_xml()
        return xml
