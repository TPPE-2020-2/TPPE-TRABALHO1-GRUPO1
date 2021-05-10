from models.sequence_diagram_element import SequenceDiagramElement
from models.lifeline import Lifeline

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

    def print_message_type(self):
        print('These are your message type options, please select one: ',
                '\n1 - Synchronous',
                '\n2 - Aynchronous',
                '\n3 - Reply')

    def add_message(self, lifelines):
        message_type_dict = {
            1: 'Synchronous',
            2: 'Assynchronous',
            3: 'Reply'
        }

        message_name = input('Insert the Message name: ')
        while len(message_name) == 0:
            print('MessageFormatException - You must define a message name')

        print('Select the source Lifeline: ')
        Lifeline().print_lifelines(lifelines)
        try:
            source_lifeline = lifelines[int(input('Which is the initial Lifeline? '))]
        except:
            print('MessageFormatException - Please select a valid Lifeline')
            source_lifeline = lifelines[int(input('Which is the initial Lifeline? '))]

        try:
            target_lifeline = lifelines[int(input('Which is the final Lifeline? '))]
        except:
            print('MessageFormatException - Please select a valid Lifeline')
            target_lifeline = lifelines[int(input('Which is the initial Lifeline? '))]

        prob = input('How much is the message probability? ')
        self.print_message_type()
        message_type = message_type_dict[int(input())]

        message = Message(name=message_name, source=source_lifeline,
                          target=target_lifeline, prob=prob,
                          message_type=message_type)
        return message