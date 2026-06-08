bill_amount = float(input("Enter the bill amount: "))
paid_amount = float(input("Enter the amount paid: "))

due_amount = bill_amount - paid_amount
if due_amount > 0:
    print("Costumer due amount : ", due_amount)

elif due_amount < 0:
    print("No due amount . Bill fully paid.")
else:
    print("Extra amount paid:" , abs(due_amount))    