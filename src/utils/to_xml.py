from models.activity_diagram import ActivityDiagram
from models.activity_diagram_element import ActivityDiagramElement
from models.sequence_diagram_element import SequenceDiagramElement
from models.fragment import Fragment
from models.message import Message
from models.transition import Transition

class ToXml():
    def __init__(self, activity_diagram):
        self.activity_diagram = activity_diagram
    
    def compute(self):
        xml = self.convert_activity_diagram_to_xml()
        return xml
    
    def convert_activity_diagram_to_xml(self):
        xml = f'<ActivityDiagram name="{self.activity_diagram.name}">\n'
        xml += self.get_tab(4) + '<ActivityDiagramElements>\n'
        for element in self.activity_diagram.elements.values():
            xml += self.get_tab(8) + self.convert_activity_diagram_element_to_xml(element) + '\n'
        xml += self.get_tab(4) + '</ActivityDiagramElements>\n'
        xml += self.get_tab(4) + '<ActivityDiagramTransitions>\n'
        for transition in self.activity_diagram.transitions.values():
            xml += self.get_tab(8) + self.convert_transition_to_xml(transition) + '\n'
        xml += self.get_tab(4) + '</ActivityDiagramTransitions>\n'
        xml += '</ActivityDiagram>\n'
        for sequence_diagram in self.activity_diagram.sequence_diagrams.values():
            xml += self.convert_sequence_diagram_to_xml(sequence_diagram)
        return xml
    
    def convert_sequence_diagram_to_xml(self, sequence_diagram):
        xml = '<SequenceDiagrams>\n'
        xml += self.get_tab(4) + '<Lifelines>\n'
        for lifeline in sequence_diagram.life_lines.values():
            xml += self.get_tab(8) + self.convert_lifeline_to_xml(lifeline) + '\n'
        xml += self.get_tab(4) + '</Lifelines>\n'
        if len(sequence_diagram.fragments) > 0:
            xml += self.get_tab(4) + '<Fragments>\n'
            for fragment in sequence_diagram.fragments:
                xml += self.get_tab(8) + self.convert_fragment_to_xml(fragment) + '\n'
            xml += self.get_tab(4) + '</Fragments>\n'
            for fragment in sequence_diagram.fragments:
                aux_sequence_diagram = fragment.sequence_diagram
                xml += self.get_tab(4) + f'<SequenceDiagram name="{aux_sequence_diagram.name}">\n'
                for message in aux_sequence_diagram.messages.values():
                    xml += self.get_tab(8) + self.convert_message_to_xml(message) + '\n'
                xml += self.get_tab(8) + f'<Fragment name="{fragment.name}"/>\n'
                xml += self.get_tab(4) + '</SequenceDiagram>\n'
        xml += '</SequenceDiagrams>\n'
        return xml
    
    def convert_activity_diagram_element_to_xml(self, element: ActivityDiagramElement):
        return f'<{element.element_type} name="{element.name}"/>'
    
    def convert_lifeline_to_xml(self, element: SequenceDiagramElement):
        return f'<Lifeline name="{element.name}"/>'
    
    def convert_transition_to_xml(self, element: Transition):
        return f'<{element.element_type} name="{element.name}" prob="{element.prob}"/>'

    def convert_fragment_to_xml(self, element: Fragment):
        return f'<Optional name="{element.name}" representedBy="{element.represented_by}"/>'
    
    def convert_message_to_xml(self, element: Message):
        return f'<Message name="{element.name}" prob="{element.prob}" source="{element.source.name}" target="{element.target.name}"/>'

    def get_tab(self, size):
        return '\t'.expandtabs(size)