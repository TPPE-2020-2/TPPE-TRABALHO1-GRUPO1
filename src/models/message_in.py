from models.user_in import UserIn
from models.message import Message

class MessageIn(UserIn):
    def __init__(self):
        self.messages = []

    def add(self, info):
        message_type_dict = {
            1: 'Synchronous',
            2: 'Assynchronous',
            3: 'Reply'
        }

        message_name = input('Insert the MESSAGE name: ')
        while len(message_name) == 0:
            print('MessageFormatException - You must define a message name')

        print('Select the source Lifeline: ')
        print_lifelines(info)
        try:

            source_lifeline = info[int(input('Which is the initial Lifeline? '))]
        except:
            print('MessageFormatException - Please select a valid Lifeline')
            source_lifeline = info[int(input('Which is the initial Lifeline? '))]

        try:
            target_lifeline = info[int(input('Which is the final Lifeline? '))]
        except:
            print('MessageFormatException - Please select a valid Lifeline')
            target_lifeline = info[int(input('Which is the initial Lifeline? '))]

        prob = input('How much is the message probability? ')
        print_message_type()
        message_type = message_type_dict[int(input())]

        message = Message(name=message_name, source=source_lifeline,
                          target=target_lifeline, prob=prob,
                          message_type=message_type)
        self.messages.append(message)

def print_lifelines(lifelines):
    print('Your Lifelines: ')
    for index, lifeline in lifelines.items():
        print('Lifeline', str(index) + ':', lifeline.name)

def print_message_type():
    print('These are your message type options, please select one: ',
          '\n1 - Synchronous',
          '\n2 - Aynchronous',
          '\n3 - Reply')