#start with a docstring to describe the porgram
"""" the echo chamber
this program will echo the input provided by the user until the user enters 'quit' or 'stop'"""

print('see your input echoed back to you, until you type quit or stop')
#the print statement above tells the user how they can interact with the program

#step 1: Set the variable exit to false
#exit condition initialised
exit = False

#step 2: While exit is equal to false:
#(while) loop is entered
while not exit:
    #step 2a: Set the variable user_input to the response to ‘How shall I greet you? ’
    #gets user input
    user_input = input('Type your input here: ')

    #step 2b: If the user_input is ‘quit’, set the variable exit to true
    #will check if the user wants to quit or stop using Boolean Operator 'or'
    if user_input == 'quit' or user_input == 'stop':
        exit = True

    #step 2c: Otherwise if user_input is 'hello' do something
    #handles specific user input and responds accordingly; in this case echoes back the user input
    elif user_input == 'hello':
        print('hello')

    #step 2d: Otherwise if user_input is 'hi' do something
    #handles specific user input and responds accordingly; in this case echoes back the user input
    elif user_input == 'hi':
        print('hi')

    #step 2e: Otherwise if user_input is 'hello?' do something
    #handles specific user input and responds accordingly; in this case echoes back the user input
    elif user_input == 'hello?':
        print('hello?')
        
print('Loop Complete!!!')
