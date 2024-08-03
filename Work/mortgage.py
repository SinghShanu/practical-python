# mortgage.py
#
# Exercise 1.7
usr_input = input("Do you want to enter extra payment details? (y/n)")
while usr_input != 'n':
    extra_payment_start_month = int(input("Enter the extra payment start month: "))
    extra_payment_end_month = int(input("Enter the extra payment end month: "))
    extra_payment = int(input("Please enter the extra payment that you want to make: "))

    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    month = 0

    while principal > 0:
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            principal = principal * (1+rate/12) - payment - extra_payment
            total_paid = total_paid + payment
            month += 1
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
            month += 1

    print("Total paid: ", round(total_paid,2))
    print("Total months: ", month)
