"""
File: fitness.py
Authors: David Mendenhall, Miles Noble, Spencer Sowby

Purpose:
    1. Asks the user to enter four values:
        a. gender
        b. birthdate in this format: YYYY-MM-DD
        c. weight in U.S. pounds
        d. height in U.S. inches
    2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
    3. Converts inches to centimeters (1 in = 2.54 cm).
    4. Calculates age, BMI, and BMR.
    5. Prints age, weight in kg, height in cm, BMI, and BMR.

    Core Requirements
        Your program contains complete and correct functions named compute_age, kg_from_lb, and cm_from_in.
        Your program contains complete and correct functions named body_mass_index and basal_metabolic_rate.
        To be correct, the basal_metabolic_rate function must compute BMR differently for males and females.
        Your program contains a function named main which gets four values from the user, calls the other functions,
        and prints the results for the user to see.

    Stretch Challenges
        Note that the stretch challenges are NOT optional :)

        Modify your program to print the height values in meters instead of centimeters.
        Modify your program to allow the user to enter weight in British stones and add a function named kg_from_stone.
        Modify your program to allow the user to enter height as U.S. feet and inches.
        Add something or change something in your program that you think would make your program better,
        easier for the user, more elegant, or more fun. Be creative.
"""

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ").upper()
    birthday = input("Enter your birthdate (YYYY-MM-DD): ")
    user_weight_input = input(
        "Do you want to enter you weight in U.S. pounds or Stones? (LB/S):").upper()
    if "LB" in user_weight_input:
        lb_weight = float(input("Enter your weight in U.S. pounds: "))
    else:
        s_weight = float(input("Enter your weight in stones: "))
    user_height_input = input(
        "Do you want to enter you height in feet or inches? (FT/IN):").upper()
    if "FT" in user_height_input:
        f_height = float(input("Enter your height in U.S. feet: "))
    else:
        in_height = float(input("Enter your height in U.S. inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthday)
    if "LB" in user_weight_input:
        kg_weight = kg_from_lb(lb_weight)
    else:
        kg_weight = kg_from_stone(s_weight)
    if "FT" in user_height_input:
        cm_height = in_per_foot(f_height)
    else:
        cm_height = cm_from_in(in_height)
    bmi = body_mass_index(kg_weight, cm_height)
    bmr = basal_metabolic_rate(gender, kg_weight, cm_height, age)

    print(f"""
Age (years): {age}
Weight (kg): {kg_weight:.2f}
Height (cm): {cm_height:.1f}
Height (m) : {cm_to_m(cm_height):.2f}
Body mass index: {bmi:.1f}
Basal metabolic rate (kcal/day): {int(bmr)}""")

    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237

    return kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches * 2.54

    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height ** 2)

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if "F" in gender:
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


def cm_to_m(cm_height):
    m = cm_height * 0.01
    return m


def kg_from_stone(stones):
    kg = 6.35029 * stones
    return kg


def in_per_foot(feet):
    inches = feet * 12
    return cm_from_in(inches)


# Call the main function so that
# this program will start executing.
main()
