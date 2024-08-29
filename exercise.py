# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here

    x = input('Enter a letter: ').lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if x in vowels:
        print(f'The letter {x} is a vowel')
    elif x.isalpha():
        print(f'The letter {x} is a consonant')
    else:
        print('Invalid entry')

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
     # Your control flow logic goes here

    try:
        age = int(input("Please enter your age: "))
        
        if age < 0:
            print('Impossible age')
        else:
            VOTING_AGE = 18
            if age >= VOTING_AGE:
                print('You are eligible to vote!')
            else:
                print('You are too young to vote!')
                
    except ValueError:
        print('Invalid input. Please enter a positive integer.')

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():

    # Your control flow logic goes here

    age = input("Input a dog's age: ")
    
    try:
        age = int(age)
        
        if age < 0:
            print('Invalid input. Please enter a positive integer.')
        elif age < 3:
            dogyears = 10.5 * age
            print(f"The dog's age in dog years is {dogyears:.1f}")
        else:
            dogyears = 21 + (7 * (age - 2))
            print(f"The dog's age in dog years is {dogyears:.1f}")
    
    except ValueError:
        print('Invalid input. Please enter a positive integer.')

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here

    # Prompt the user to enter if it is cold
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()
    
    # Determine clothing advice based on conditions
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif cold == "no" and raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here

    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = input("Enter the day of the month: ")
    day = int(day);
    if (month == "dec" and day in range(21, 32)) or (month == "jan" and day in range(1, 32)) or (month == "feb" and day in range(1, 32)):
        season = "Winter"
        print(f"{month} {day} is in {season}.")
    elif (month == "mar" and day in range(1, 20)) or (month == "apr" and day in range(1, 30)) or (month == "jun" and day in range(1, 20)):
        season = "sprting"
        print(f"{month} {day} is in {season}.")
    elif (month == "jun" and day in range(21, 30)) or (month == "jul" and day in range(1, 30)) or (month == "aug" and day in range(1, 30)) or (month == "sep" and day in range(1, 21)):
        season = "Summer"
        print(f"{month} {day} is in {season}.")
    elif (month == "sep" and day in range(22, 31)) or (month == "oct" and day in range(1, 31)) or (month == "nov" and day in range(1, 31)) or (month == "dec" and day in range(1, 20)):
        season = "Fall"
        print(f"{month} {day} is in {season}.")
    else:
        print("Invalid date.")

# Call the function
determine_season()