from errors.errors import OrderError, MissMergeError
from time import sleep
from utils.to_xml import ToXml

class Util():
    def __init__(self):
        self.START_NODE = 'StartNode'
        self.ACTIVITY_NODE = 'Activity'
        self.TRANSITION_NODE = 'Transition'
        self.DECISION_NODE = 'DecisionNode'
        self.MERGE_NODE = 'MergeNode'
        self.END_NODE = 'EndNode'
        self.LIFELINE = 'LifeLine'
        self.MESSAGE = 'Message'
        self.FRAGMENT = 'Fragment'

    def check_start_node_existence(self, nodes, node_type):
        node_exist = False
        for element in nodes.values():
            if(element.element_type == self.START_NODE):
                node_exist = True
                break
        if(node_exist and node_type == self.START_NODE):
            raise OrderError('Start node already exits')
        if(not node_exist and node_type != self.START_NODE):
            raise OrderError('Start node does not exits')
        return node_exist

    def check_end_node_existence(self, nodes):
        node_exist = False
        for element in nodes.values():
            if(element.element_type == self.END_NODE):
                node_exist =  True
                break
        if(not node_exist):
            raise OrderError('End node does not exits')
        return node_exist
    
    def check_join_possibility(self, nodes):
        decision_count = 0
        merge_count = 0
        for element in nodes.values():
            if(element.element_type == self.DECISION_NODE):
                decision_count+=1
            elif(element.element_type == self.MERGE_NODE):
                merge_count+=1
        if(not decision_count or merge_count >= decision_count):
            raise OrderError('It\'s not posible to create a merge node because does ' \
                             'not exits any match decision node.')

        return True
    
    def check_close_possibility(self, nodes):
        decision_count = 0
        merge_count = 0
        for element in nodes.values():
            if(element.element_type == self.DECISION_NODE):
                decision_count+=1
            elif(element.element_type == self.MERGE_NODE):
                merge_count+=1
        if(decision_count != merge_count):
            raise MissMergeError('You need close all decisions node before end your diagram')
        return True
    
    def clear(self):
        for i in range(1, 20):
            print()
        return 0

    def print_and_clear(self, message, clear=True):
        if(clear):
            self.clear()
        print('-'*64)
        print(message)
        print('-'*64)
        sleep(2)
   
    def generate_diagram(self, activity_diagram):
        try:
            self.check_start_node_existence(activity_diagram.get_elements(), None)
            self.check_end_node_existence(activity_diagram.get_elements())
        except OrderError as e:
            raise OrderError(e)
        to_xml = ToXml(activity_diagram)
        xml = to_xml.compute()
        f = open(f"xmls/{activity_diagram.name}.xml", "w+")
        f.write(xml)
        f.close()

    def get_tab(self, size):
        return '\t'.expandtabs(size)
