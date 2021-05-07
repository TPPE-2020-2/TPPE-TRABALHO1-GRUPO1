from models.activity_diagram_element import ActivityDiagramElement

class Transition(ActivityDiagramElement):
    def __init__(self, name='', prob=-1, source=None, target=None, element_type=''):
      super().__init__(name, element_type)
      self.source = source
      self.target = target
      self.prob = prob

    def __eq__(self, transition):
        return self.name == transition.name and \
                self.prob == transition.prob and \
                self.source == transition.source and \
                self.target == transition.target and \
                self.element_type == transition.element_type

    def __str__(self):
        str_message = r'{' + f'Name: {self.name}, Prob: {self.prob}, ' 
        if self.source:
            str_message += f'Source: {self.source.name}, '
        if self.target:
            str_message += f'Target: {self.target.name}, '
        str_message += f'Element type: {self.element_type}' + r'}'
        return str_message

    def get_source(self):
        return self.source
   
    def set_source(self, source):
        self.source = source

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_prob(self):
        return self.prob

    def set_prob(self, prob):
        self.prob = prob
