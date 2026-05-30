# Program to check student enrollment eligibility
def check_enrollment():
    try:
        # Get age input from the user
        age = int(input("Enter the student's age: "))

        # Logic for age validation (10 to 20 years inclusive)
        if 10 <= age <= 20:
            print("Enrolment successful! Welcome to the class.")
        else:
            print("Sorry, you cannot enrol. Age must be between 10 and 20.")
            
    except ValueError:
        print("Invalid input. Please enter a numerical age.")

# Run the program
check_enrollment()
