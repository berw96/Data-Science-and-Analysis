

_is_running = True
_is_paused = False
_console_input = ""

# The application loop consists of a while loop initiated and stopped with a boolean variable.
# This variable may be set using using user input such as keypress events or console input.
while _is_running:
    # Use console input to interface with application loop
    _console_input = input()
     
    # Code to run if application is not paused
    if _is_paused:
        # Continue running the application loop, but cease all usual actions
        # Allow only unpausing or menu/HUD traversal
        if _console_input.__contains__("resume"):
            print("Resuming application...")
            _is_paused = False
        else:
            print("\'{}\' is not a recognised command whilst application is paused.".format(_console_input))
            print("Try \'resume\'.")
    else:
        # Commence with application functionality
        if _console_input.__contains__("stop"):
            print("Stopping application loop...")
            _is_running = False
        elif _console_input.__contains__("pause"):
            print("Pausing application...")
            _is_paused = True
        else:
            print("You typed {}".format(_console_input))
            print("Going")
        
    
    

# Will not print whilst while loop is running
print("Application stopped, goodbye.")
