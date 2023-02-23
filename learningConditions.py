# if statement
# we have a text
# if it's hot
     # It's a hot day
     # Drink plenty of water
#otherwise if it's cold
     # It's a cold day
     # Wear warm clothes
# otherwise
     # It's a lovely day

# 1. define a variable

is_hot = False
is_cold = False # having both as False will print the else statement
if is_hot: # this is a condition hence :
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

# excercise: price of a house is $1,
# if buyer has a good credit
# they need to put down 10%
# Otherwise they need to put down 20%
# print the down payment

house_price = 1000000
good_credit = False

if good_credit:
    deposit = house_price * 0.1
    print("Deposit for house is ")
else:
     deposit = house_price * 0.2
print("Deposit for house is: $", deposit) # or print(f"Deposit payment: ${deposit}") - concatenated

# LOGICAL OPERATORS AND OR
#eg if applicant has high income AND good credit Eligible for loan = we have 2 conditions income and credit
# if both true then he gets loan

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")

#the same example where applicant has high income OR good credit

has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
y
# NOT operator
# if applicant has a good credit AND doesn't have a criminal record


has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible")










