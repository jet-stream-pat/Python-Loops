#start with a docstring to describe the porgram
"""" The pointless loop will continue to ask for user input until the user enters 'quit'"""

#step 1: Set the variable exit to false
#exit condition initialised
exit = False

#step 2: While exit is equal to false:
#(while) loop is entered
while not exit:
    #step 2a: Set the variable user_input to the response to ‘How shall I greet you? ’
    #gets user input
    user_input = input('How shall I greet you? ')

    #step 2b: If the user_input is ‘quit’, set the variable exit to true
    #will check if the user wants to quit
    if user_input == 'quit':
        exit = True

    #step 2c: Otherwise if user_input is 'hello' do something
    #handles specific user input and responds accordingly
    elif user_input == 'hello':
        print('Hello to you too!')

    #step 2d: Otherwise if user_input is 'hi' do something
    #handles specific user input and responds accordingly
    elif user_input == 'hi':
        print('Hi there')

    #step 2e: Otherwise if user_input is 'hello?' do something
    #handles specific user input and responds accordingly
    elif user_input == 'hello?':
        print('Hello, can I help you?')
        
print('Loop Complete! Adios!')
#print statement when 'quit' is entered by the user (note back to no idententation)

#code tested in shell and this is correct :)
#code does as expected, and required with activity 2.16
