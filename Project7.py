#---------------------
# Summer Davis
# COSC 1336
# Project 7
#---------------------
# Objective: Program will display the user's initials,
# email address, and last 4 digits of their SSN.
#
# Program will:
# - ask user to enter last name, first name, and SSN
# - use input data to create an input dictionary
# - use input dictionary to generate
#   an identity dictionary with the following keys:
# -> user's initials, uppercase
# -> email address (first initial, last name, @gmail.com), lowercase
# -> last 4 digits of SSN
# - Generate & display a summary of the identity dictionary 
# 
#---------------------

# Display the start of the project
def header ():
    print('\n')
    print('Lottery Commissioner\'s Entry')
    print('-' * 80)

# Collect and organize all of the program tasks
def main():
    
    # Header of the project
    header()

    # Collect data and create input dictionary
    personEntry = createDict()

    # Create identity dictionary
    personID = createID(personEntry)

    # Display summary
    displayResult(personID)
    
    # End of project display
    footer()


# Display identity summary
def displayResult(personID):
    print('\n')
    print('-' * 80)
    print('Summary: Create Identity')
    print('-' * 80)
    print('The person\'s')

    for key in personID:
        print(f'  {key}: {personID[key]}')


# Generate a new identity
def createID(personEntry):
    ID = {}
    ID['User\'s initial'] = personEntry['First'][0].upper() + \
                            personEntry['Last'][0].upper()
    
    ID['Email address'] = personEntry['First'][0].lower() + \
                          personEntry['Last'].lower() + \
                          '@gmail.com'
    
    ID['Last 4-digit of SSN'] = personEntry['SSN'][-4:]

    return ID
    

# Collect data - create and return a dictionary
def createDict():
    person = {}
    person['Last'] = getStringData('Enter last name ')
    person['First'] = getStringData('Enter first name ')
    person['SSN'] = getStringData('Enter SSN ')

    return person

# Get users entry of string data
def getStringData(prompt):
    while (True):
        value = input(prompt)
        return  value


# Get users entry of ONLY float data
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value

        except ValueError: 
            print('\n\tError Msg: Non Numbers entered.')

# Get users entry of ONLY integer data
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError: 
            print('\n\tError Msg: Non Integers entered.')
    
# Display the end of the project
def footer():
    print('\n')
    print(' '+'-' * 80)
    print('End of Project 7')

# Call the main function  
main()
