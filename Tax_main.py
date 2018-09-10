# This program is intended to provide after tax income given an input from the user

import aftertax

income = int(input("What is your annual income? "))
state_ID = input("What is your state abbreviation? ")
filing_status = input("What is your filing status for this tax year? ")

if state_ID == "IN" and filing_status == "individual":
    print(aftertax.indv(income))
elif state_ID == "IN" and filing_status == "married filing jointly":
    print(aftertax.mfj(income))
else:
    print("Your state is not yet supported, sorry for the inconvenience.")
