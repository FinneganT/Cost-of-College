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


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = int(input("Enter the total cost for a year: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the credits for the semster: "))

    while True:
        # Show your menu here.
        print("Cost of college breakdown")
        print("1. Cost per semster")
        print("2.Cost per month")
        print("3. Cost for one class")
        print("4. Cost per credit")
        print("5. Cost per CS1430 class day")
        print("6. Worth it?")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "Q":
            print("Exit program.")
            break
        
            

        # Add a branch for each menu option here.
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: {cost_per_month(annual_cost):.2f}")
        elif choice =="3":
            print(f"Cost for one class : {cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: {cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per CS1430 class: {cost_per_class(annual_cost, credits):.2f}")
        #elif choice == "6":

        else:
            print("Invalid choice.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
