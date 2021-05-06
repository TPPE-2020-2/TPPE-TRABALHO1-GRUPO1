import unittest
from utils.utils import Util
from models.activity_diagram import ActivityDiagram
from models.activity_diagram_element import ActivityDiagramElement
from models.transition import Transition
from models.sequence_diagram import SequenceDiagram
from models.fragment import Fragment
from models.message import Message
from models.lifeline import Lifeline
from parameterized import parameterized
from errors.errors import OrderError, MissMergeError


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.util = Util()

    @parameterized.expand([
        [{'A1': ActivityDiagramElement(name='A1', element_type=Util().START_NODE),
          'A2': ActivityDiagramElement(name='A2', element_type=Util().TRANSITION_NODE)}],
        [{'B1':ActivityDiagramElement(name='B1', element_type=Util().START_NODE), \
          'B2': ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
          'B3': ActivityDiagramElement(name='B3', element_type=Util().MERGE_NODE)}],
        [{'C1': ActivityDiagramElement(name='C1', element_type=Util().START_NODE)}],
    ])
    def test_check_start_node_existence_true(self, nodes):
        response = self.util.check_start_node_existence(nodes, None)
        self.assertTrue(response)
    
    @parameterized.expand([
        [{'A1': ActivityDiagramElement(name='A1', element_type=Util().END_NODE), \
          'A2': ActivityDiagramElement(name='A2', element_type=Util().TRANSITION_NODE)}],
        [{'B1':ActivityDiagramElement(name='B1', element_type=Util().MERGE_NODE), \
         'B2': ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
         'B3': ActivityDiagramElement(name='B3', element_type=Util().MERGE_NODE)}],
        [{'C1': ActivityDiagramElement(name='C1', element_type=Util().ACTIVITY_NODE)}],
    ])
    def test_check_start_node_existence_false(self, nodes):
        with self.assertRaises(OrderError):
          response = self.util.check_start_node_existence(nodes, None)

    @parameterized.expand([
        [{'A1': ActivityDiagramElement(name='A1', element_type=Util().START_NODE), \
          'A2': ActivityDiagramElement(name='A2', element_type=Util().DECISION_NODE)}],
        [{'B1':ActivityDiagramElement(name='B1', element_type=Util().START_NODE), \
         'B2': ActivityDiagramElement(name='B2', element_type=Util().DECISION_NODE), \
         'B3': ActivityDiagramElement(name='B3', element_type=Util().DECISION_NODE)}],
        [{'C1': ActivityDiagramElement(name='C1', element_type=Util().DECISION_NODE)}],
    ])
    def test_check_join_possibility(self, nodes):
        response = self.util.check_join_possibility(nodes)
        self.assertTrue(response)
    
    @parameterized.expand([
        [{'A1': ActivityDiagramElement(name='A1', element_type=Util().START_NODE), \
          'A2': ActivityDiagramElement(name='A2', element_type=Util().MERGE_NODE)}],
        [{'B1':ActivityDiagramElement(name='B1', element_type=Util().START_NODE), \
         'B2': ActivityDiagramElement(name='B2', element_type=Util().MERGE_NODE), \
         'B3': ActivityDiagramElement(name='B3', element_type=Util().MERGE_NODE)}],
        [{'C1': ActivityDiagramElement(name='C1', element_type=Util().START_NODE)}],
    ])
    def test_check_join_possibility_false(self, nodes):
        with self.assertRaises(OrderError):
          response = self.util.check_join_possibility(nodes)

    def test_generate_diagram(self):
        activity_diagram = self.mock_activity_diagram(True, True, True)
        print(activity_diagram)
        self.assertTrue(True)

    def mock_activity_diagram(self, has_activity=False, has_fragment=False, has_multiple_fragments=False):
        activity_diagram = ActivityDiagram(name='ActivityDiagram1')
        # Start Node
        start_node = ActivityDiagramElement(name='StartNode1', element_type=self.util.START_NODE)
        activity_diagram.set_elements(start_node)
        activity_diagram.set_start_node(start_node)
        # Decision Node        
        decision_node = ActivityDiagramElement(name='DecisionNode1',
                                                element_type=self.util.DECISION_NODE)
        activity_diagram.set_elements(decision_node)
        activity_diagram.set_transitions(self.create_transition(name='FirstTr', source_node=start_node,
                                                          target_node=decision_node))
        # Merge Node
        merge_node = ActivityDiagramElement(name='MergeNode1', element_type=self.util.MERGE_NODE)
        activity_diagram.set_elements(merge_node)
        activity_diagram.set_transitions(self.create_transition(name='Tr2', source_node=decision_node,
                                                          target_node=merge_node))
        last_node = merge_node
        if has_activity:
            activity_node = ActivityDiagramElement(name='ActivityNode1', element_type=self.util.ACTIVITY_NODE)
            activity_diagram.set_elements(activity_node)
            activity_diagram.set_transitions(self.create_transition(name='Tr3',
                                                                    source_node=merge_node,
                                                                    target_node=activity_node))
            last_node = activity_node
            sequence_diagram = self.mock_sequence_diagram(has_fragment, has_multiple_fragments)
            activity_diagram.set_sequence_diagrams(sequence_diagram)
      
        # EndNode
        end_node = ActivityDiagramElement(name='EndNode1', element_type=self.util.END_NODE)
        activity_diagram.set_elements(end_node)
        activity_diagram.set_transitions(self.create_transition(name='LastTr', source_node=last_node,
                                                          target_node=end_node))
        return activity_diagram

    def mock_sequence_diagram(self, has_fragment, has_multiple_fragments):
        sequence_diagram = SequenceDiagram(name='SequenceDiagram', guard_condition=True)
        
        # LifeLines
        lifelines = {0 : Lifeline(id=0, name='LifeLineXs')}
        sequence_diagram.set_life_lines(lifelines)
        
        # Message
        message = Message(name='MensagemX', source=lifelines[0],
                      target=lifelines[0], prob=0.5,
                      message_type='Synchronous')
        sequence_diagram.set_messages(message)

        if has_fragment:
            fragment = Fragment(name='Fragment1',
                                represented_by=sequence_diagram.name,
                                sequence_diagram=sequence_diagram)
            sequence_diagram.set_fragments(fragment)
        if has_multiple_fragments:
            fragment = Fragment(name='Fragment1',
                                represented_by=sequence_diagram.name,
                                sequence_diagram=self.mock_sequence_diagram(False, False))
            sequence_diagram.set_fragments(fragment)
        
        if has_fragment:
            sequence_diagram.get_fragments()[0].sequence_diagram = sequence_diagram
        
        return sequence_diagram

    def create_transition(self, name, source_node, target_node):
        return Transition(name=name,
                          prob=0.5,
                          source=source_node, 
                          target=target_node, 
                          element_type=self.util.TRANSITION_NODE)