import math

# This program allows the user to access two different financial calculators:
# an investment calculator or a home loan repayment calculator.

# the user is allowed to choose which calculator they want to use.
calculator_choice = ""
while calculator_choice.lower() != "investment" and calculator_choice.lower() != "bond":
    # while name is different from the two options (use lower() to avoid case sensitivity) - use while to loop until an adequate option is picked
    calculator_choice = input("Calculator Options: \n"  # use \n for a new line and \t for tabspace
                              "investment \t- to calculate the amount of interest you'll earn on your investment. \n"
                              "bond \t \t- to calculate the amount you'll have to pay on a home loan. \n"
                              "\n"
                              "Choose either \'investment\' or \'bond\' from the menu above to proceed: ")

    if calculator_choice.lower() != "investment" and calculator_choice.lower() != "bond":   #display error message
        print()
        print("Error: you have entered an invalid input. Try again.")
    print()

# calculations for the investment calculator:
if calculator_choice.lower() == "investment":
    deposit_amount = float(input("Please enter the amount of money you are depositing (R): "))
    interest_rate = float(input("Please enter the numerical value of the percentage of the interest rate (e.g. 8 for 8%): "))
    years_investment = float(input("Please enter the number of years you plan on investing: "))

    interest = input("Are you interested in \'simple\' or \'compound\' interest? ")

    # check spelling of input
    while interest.lower() != "simple" and interest.lower() != "compound":
        print("Error: you have entered an invalid input. Please type only \'simple' or \'compound\'. Try again.")
        print()
        interest = input("Are you interested in \'simple\' or \'compound\' interest? ")

    if interest.lower() == "simple":
        total = deposit_amount * (1 + (interest_rate/100) * years_investment)

    else:
        total = deposit_amount * math.pow((1+(interest_rate/100)), years_investment)

    print()
    print("The total amount after the investment will be:", round(total, 2), "R")


# calculations for the bond calculator:
if calculator_choice.lower() == "bond":
    house_value = float(input("Please enter the current value of the house (R): "))
    interest_rate = float(input("Please enter the numerical value of the percentage of the annual interest rate (e.g. 8 for 8%): "))
    repayment_period = float(input("Please enter the number of months you plan to take to repay the bond: "))

    interest_rate = interest_rate / 100     #this is becasue 8% is equal to 0.008
    monthly_interest_rate = interest_rate / 12  #the formula provided specifically asks for the monthly interest rate, which is the annual one divided by 12

    monthly_repayment = (monthly_interest_rate * house_value) / ( 1 - math.pow((1+monthly_interest_rate), (-(repayment_period))))

    print()
    print("The amount you will have to repay each month is:", round(monthly_repayment, 2), "R")