def shutdown():
    # Get input from the user
    user_input = input("Enter 'Yes' to shut down, 'no' to abort: ")
    
    # Check conditions
    if user_input == "Yes":
        print("shutting down")
    elif user_input == "no":
        print("abort shut down")
    else:
        print("sorry.")

# Call the function
shutdown()
