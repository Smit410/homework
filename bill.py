def give_change(bill, paid):
    return paid - bill

total = float(input("Bill amount: "))
given = float(input("Amount paid: "))

change = give_change(total, given)

print("Return to customer: $", change)