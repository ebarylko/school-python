#Function Practice
#EItan


def income_tax(income):
    #pre: takes no arguments
    #post: returns the product of income and the tax in the bracket if income is valid, otherwise returns "Not Valid"
    bracket = [(0, 49021, 0.15),
               (49021, 98041, 20.5),
               (98041, 151979, 0.26)]
    tax = [t for a, b, t in bracket if income in range(a, b)]
    return tax[0]*income 

def taxed_income():
    #pre: Takes nothing
    #post: returns a message after asking for income with the tax
    income = int(input("What is your income: "))
    if income not in range(0, 151979):
        print("Sorry, not sure how to calculate that income tax")
    else:
        print("Your income tax is", income_tax(income))
