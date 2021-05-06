# from unittest import mock, TestCase
# from unittest.mock import call
# import main
# from parameterized import parameterized

# class TestMain(TestCase):
#     # Test main
#     def test_create_activity_diagram(self):
#         with mock.patch('builtins.input', side_effect=['1', 'Name', '7', '3']):
#             with mock.patch('builtins.print') as _print:
#                 main.main()
#                 _print.assert_any_call('----- Activity Diagram -----')

#     def test_create_sequence_diagram(self):
#         with mock.patch('builtins.input', side_effect=['2', 'Name', '4', '3']):
#             with mock.patch('builtins.print') as _print:
#                 main.main()

#     def test_exit(self):
#         with mock.patch('builtins.input', return_value='3'):
#             with mock.patch('builtins.print') as _print:
#                 main.main()
#                 _print.assert_called_with('Leaving the program!')
    
#     def test_default(self):
#         with mock.patch('builtins.input', side_effect=['a', '3']):
#             with mock.patch('builtins.print') as _print:
#                 main.main()
#                 _print.assert_any_call('Invalid input. Please select again\n')
       

#     # Test activity_diagram_menu

