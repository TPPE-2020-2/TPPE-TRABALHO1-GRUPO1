from models.sequence_diagram_element import SequenceDiagramElement
from utils.utils import Util
util = Util()

class SequenceDiagram():
    def __init__(self, name='', guard_condition=''):
        self.name = ''
        self.guard_condition = ''
        self.life_lines = []
        self.messages = []
        self.fragments = []

    def __eq__(self, sequence_diagram): # pragma: no cover
        return self.name == sequence_diagram.name and \
        self.guard_condition == sequence_diagram.guard_condition and \
        self.life_lines == sequence_diagram.life_lines and \
        self.messages == sequence_diagram.messages and \
        self.fragments == sequence_diagram.fragments
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nGuard Condition: {}\nLife Lines: {}\nElements: {}\n'.format(self.name, \
                                                                                self.start_node, \
                                                                                self.life_lines, \
                                                                                self.messages, \
                                                                                self.fragments)

    def dispose(self):
        self.name = ''
        self.guard_condition = ''
        self.life_lines = {}
        self.messages = []
        self.fragments = []

    def set_name(self, name):
        self.name = name
    
    def set_guard_condition(self, guard_condition):
        self.guard_condition = guard_condition

    def set_life_lines(self, life_line):
        self.life_lines = life_line
    
    def set_messages(self, messages):
        self.messages.append(messages)

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

    def to_xml(self):
        xml = '<SequenceDiagrams>\n'
        xml += util.get_tab(4) + '<Lifelines>\n'
        for lifeline in self.life_lines.values():
            xml += util.get_tab(8) + f'<Lifeline name="{lifeline.name}">' + '\n'
        xml += util.get_tab(4) + '<\Lifelines>\n\n'
        xml += util.get_tab(4) + '<Fragments>\n'
        for fragment in self.fragments:
            xml += util.get_tab(8) + f'<Optional name="{fragment.name} representedBy="{self.name}">\n'
        xml += util.get_tab(4) + '</Fragments>\n'
        xml += util.get_tab(4) + f'<SequenceDiagram name="{self.name}">\n'
        for message in self.messages:
            xml += util.get_tab(8) + f'{message.to_xml()}\n'
        xml += util.get_tab(8) + f'<Fragment name="{fragment.name}">\n'
        xml += util.get_tab(4) + '</SequenceDiagram>\n\n'
        xml += '</SequenceDiagrams>\n'

        print(xml)
        return xml