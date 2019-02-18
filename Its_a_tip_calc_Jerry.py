# ask the customer what's the damage?
total_bill = float(input("What was the total bill? "))
# and how's the service?
service = str(input("Was the service 'good', 'bad', or 'fair'? "))
# and who's paying
per_person = int(input("And how many of you are paying? "))
# function that prints out the amounts needed for any bill, service,
# and people
if service == "good":
    print("Good service. \nTip Amount: $%.2f" %(total_bill * .2))
    print("Total Amount: $%.2f" % (total_bill * 1.2))
    print("Total Per Person: $%.2f" % (total_bill *1.2/per_person))
elif service == "bad":
    print("Bad service. \nTip Amount: $%.2f" %(total_bill * .1))
    print("Total Amount: $%.2f" % (total_bill * 1.1))
    print("Total Per Person: $%.2f" % (total_bill *1.1/per_person))
elif service == "fair":
    print("Fair service. \nTip Amount: $%.2f" %(total_bill * .15))
    print("Total Amount: $%.2f" % (total_bill * 1.15))
    print("Total Per Person: $%.2f" % (total_bill *1.15/per_person))



