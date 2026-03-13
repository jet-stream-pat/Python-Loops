# Step 1: Set the variable exit to false
exit = False

# Step 2: While exit is equal to false:
while not exit:
    # Step 2a: Set the variable user_input to the response to ‘Type your input here: ’
    user_input = input("Type your input here: ").strip().lower()
    
    # Step 2b: If the user_input is ‘quit’, set the variable exit to true
    if user_input == "quit":
        exit = True
    # Step 2c: Otherwise if user_input has some value(s) do something
    elif user_input == "hello":
        print("Hello to you too!")
    # Step 2d: Otherwise if user_input has some other value(s) do something else
    elif user_input == "bye":
        print("Goodbye!")
    # Step 2e: Add more conditions as needed
    # ...
    # Step 2f: Otherwise do something else
    else:
        print("I don't understand that command.")
        
print("Loop has ended. Goodbye!")
