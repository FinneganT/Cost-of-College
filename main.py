"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost/SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost/ MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return cost_per_semester(annual_cost)/ CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
  
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost)/ credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    CS1430_course_cost = cost_per_credit(annual_cost, credits) * CS1430_CREDITS
    return CS1430_course_cost / CS1430_MEETINGS_PER_SEMESTER 


def worth_it(annual_cost, credits, game_price):
    """Gives back how many videos game one CS1430 class is worth."""
    return cost_per_class(annual_cost, credits) / game_price


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = float(input("Enter the total cost for a year: "))
    while annual_cost <= 0:
        annual_cost = float(input("Annual cost must be more than 0, Try again: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the credits for the semester: "))
    while credits <= 0:
        credits = input("Amount of credits must be more than 0, try again: ")

    while credits <= 0:
        credits = int(input("Enter a credit amount more than 0, Try again please: "))

    while True:
        # Show your menu here.
        print("-" * 10 + "Cost of college breakdown" + "-" * 10)
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost for one class day")
        print("4. Cost per credit")
        print("5. Cost per CS1430 class period")
        print("6. Worth it?")
        print("Q. Quit")
        choice = input("Choose an option: ").strip().upper()

        if choice == "Q":
            print("Exit program.")
            break
        
            

        # Add a branch for each menu option here.
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice =="3":
            print(f"Cost for one class day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per CS1430 class period: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            game_price = float(input("Price of video game: "))
            while game_price <= 0:
                game_price = float(input("The price must be more than 0, Enter a valid input: "))
            per_class = cost_per_class(annual_cost, credits)
            games = worth_it(annual_cost, credits, game_price)
            print(f"One CS1430 class costs: ${per_class:.2f}")
            print(f"That would equal {games:.2f} new video games!")
        else:
            print("Invalid choice.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
