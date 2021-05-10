from models.sequence_diagram_element import SequenceDiagramElement

class Lifeline(SequenceDiagramElement):
    def __init__(self, id=-1, name=''):
        super().__init__(name)
        self.id = id

    def __eq__(self, life_line): # pragma: no cover
        return self.name == life_line.name and \
                self.id == life_line.id
    
    def __str__(self): # pragma: no cover
        return 'ID: {}\nName: {}\n'.format(self.id, self.name)

    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

    def get_lifelines(self):
        lifelines = {}
        lifelines_amount = input('Insert the number of lifelines: ')
        for index, lifeline in enumerate(range(int(lifelines_amount))):
            lifeline_name = input(f'Insert the {index + 1} Lifeline name: ')
            lifeline = Lifeline(id=index, name=lifeline_name)
            lifelines[index] = lifeline
        return lifelines
    
    def print_lifelines(self, lifelines):
        print('Your Lifelines: ')
        for index, lifeline in lifelines.items():
            print('Lifeline', str(index) + ':', lifeline.name)
