'''Practical Task 1 - OOP Classes'''
### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Initialise the instance variables for emails.
    email_address = ''
    subject_line = ''
    email_content = ''
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(has_been_read):
        has_been_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email('example@hyperion.com', 'Subject: class', 'Body: Feedback available, check your dashboard')
    email_2 = Email('example@support.com', 'Subject: Mentorship', 'Body: Hours available now with our experts')
    email_3 = Email('example@contactus.com', 'Subject: Interview Software engineer', 'Body: Hi, Are you available this thursday?')
    inbox.append(email_1, email_2, email_3)
def list_emails(n):
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    if n == 0:
        print('0 - ' + populate_inbox.email_1.subject_line)
    elif n == 1:
        print('1 - ' + populate_inbox.email_2.subject_line) 
    elif n == 2:
        print('2 - ' + populate_inbox.email_3.subject_line)

def read_email(index):
    # Create a function which displays a selected email. 
    if index == 0:
        print(inbox[0])
    elif index == 1:
        print(inbox[1])
    elif index == 2:
        print(inbox[2])            
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    inbox[index].has_been_read = True
# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        
    elif user_choice == 2:
        # add logic here to view unread emails
            
    elif user_choice == 3:
        # add logic here to quit appplication

    else:
        print("Oops - incorrect input.")