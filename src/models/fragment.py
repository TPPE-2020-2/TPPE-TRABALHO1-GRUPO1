from models.sequence_diagram_element import SequenceDiagramElement
class Fragment(SequenceDiagramElement):
    def __init__(self, name='', represented_by=None, sequence_diagram=None):
        super().__init__(name)
        self.represented_by = represented_by
        self.sequence_diagram = sequence_diagram

    def __eq__(self, fragment): # pragma: no cover
        return self.name == fragment.name and \
                self.represented_by == fragment.represented_by and \
                self.sequence_diagram == fragment.sequence_diagram
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nRepresented by: {}\n'.format(self.name, self.represented_by)

    def set_represented_by(self, represented_by):
        self.represented_by = represented_by
    
    def get_represented_by(self):
        return self.represented_by

    def set_sequence_diagram(self, sequence_diagram):
        self.sequence_diagram = sequence_diagram
    
    def get_sequence_diagram(self):
        return self.sequence_diagram