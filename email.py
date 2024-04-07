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
    email_1 = Email('example@hyperion.com', 'Submission graded', 'Feedback available, check your dashboard.')
    email_2 = Email('example@hyperionsupport.com', 'Mentorship programming', 'Hours available now with our experts.')
    email_3 = Email('example@contactus.com', 'Interview Software engineer', 'Hi, Are you available this thursday?')
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)

def list_emails(inbox):
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for index, email in enumerate(inbox, 0):
        print(index, email.subject_line)

def read_email(index):
    # Create a function which displays a selected email. 
    if index == 0:
        print(inbox[index])
    elif index == 1:
        print(inbox[index])
    elif index == 2:
        print(inbox[index]) 
    else:
        print('Incorrect input. Try again')           
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    inbox[index].has_been_read = True
    print(f"\nEmail from {inbox[index].email_address} has been read!")
# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True

while menu == True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        menu = False
        list_emails(inbox) #subjects
        index = int(input('\nPlease select email to read - enter number: '))
        # take all attributes of selected email class and combine into one string, then print that string
        email_summary = inbox[index].email_address + '\n' + inbox[index].subject_line + '\n' + inbox[index].email_content 
        print(email_summary)
        inbox[index].has_been_read = True
        menu = True

    elif user_choice == 2:
        # add logic here to view unread emails
        menu = False
        
        reads = []
        for email in inbox:
            reads.append(email.has_been_read)

        all_emails_read = all(reads)

        if all_emails_read == True:
            print('No unread emails.')
        else:
            for email in inbox:
                if email.has_been_read == False:    # If email boolean False, then message should be in the list
                    print(str(inbox.index(email)) + ' ' + str(email.subject_line))
        menu = True

    elif user_choice == 3:
        # add logic here to quit appplication
        print('The mail app will close now')
        menu = False

    else:
        print("Oops - incorrect input.")
        menu = True