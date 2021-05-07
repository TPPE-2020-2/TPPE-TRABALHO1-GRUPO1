from models.sequence_diagram_element import SequenceDiagramElement
class Message(SequenceDiagramElement):
    def __init__(self, name='', source=None, target=None, prob=0, message_type=''):
        super().__init__(name)
        self.source = source
        self.target = target
        self.prob = prob
        self.message_type = message_type
    
    def __eq__(self, message): # pragma: no cover
        return self.name == message.name and \
                self.source == message.source and \
                self.target == message.target and \
                self.prob == message.prob and \
                self.message_type == message.message_type
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nSource: {}\nTarget: {}\nProb: {}\nMessage Type: {}\n'.format(self.name, \
                                                                                        self.source, \
                                                                                        self.target, \
                                                                                        self.prob, \
                                                                                        self.message_type)

    def set_source(self, source):
        self.source = source
    
    def set_target(self, target):
        self.target = target
    
    def set_prob(self, prob):
        self.prob = prob

    def set_message_type(self, message_type):
        self.message_type = message_type

    def get_source(self):
        return self.source
    
    def get_target(self):
        return self.target
    
    def get_prob(self):
        return self.prob

    def get_message_type(self):
        return self.message_type
