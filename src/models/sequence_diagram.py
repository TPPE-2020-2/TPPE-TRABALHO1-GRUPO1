from models.sequence_diagram_element import SequenceDiagramElement
from models.lifeline import Lifeline


class SequenceDiagram:

    def initialize_attributes(self, guard_condition, name):
        self.name = name
        self.guard_condition = guard_condition
        self.life_lines = {}
        self.messages = {}
        self.fragments = []

    def equality(self, sequence_diagram):
        return self.name == sequence_diagram.name and \
               self.guard_condition == sequence_diagram.guard_condition and \
               self.life_lines == sequence_diagram.life_lines and \
               self.messages == sequence_diagram.messages and \
               self.fragments == sequence_diagram.fragments

    def __init__(self, name='', guard_condition=''):
        self.initialize_attributes(guard_condition, name)

    def __eq__(self, sequence_diagram):  # pragma: no cover
        return self.equality(sequence_diagram)

    def __str__(self):  # pragma: no cover
        return 'Name: {}\nGuard Condition: {}\nLife Lines: {}\nElements: {}\n'.format(self.name, self.guard_condition,
                                                                                      self.life_lines, self.messages,
                                                                                      self.fragments)

    def dispose(self):
        self.initialize_attributes('', '')

    def set_name(self, name):
        self.name = name

    def set_guard_condition(self, guard_condition):
        self.guard_condition = guard_condition

    def set_life_lines(self, life_lines: dict):
        self.life_lines = life_lines

    def set_messages(self, messages):
        if type(messages) == type([]):
            for message in messages:
                self.messages[message.get_name()] = message
        else:
            self.messages[messages.get_name()] = messages

    def set_fragments(self, fragments):
        if type(fragments) == type([]):
            self.fragments = [*self.fragments, *fragments]
        else:
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
