import math


def round_str(number):
    return str(round(number))


def payments(amount, interest_rate_percents, n_years, monthly_payment, extra_payment=0):
    disable_labels = False
    label_month = "" if disable_labels else "month: "
    label_remaining_amount = "" if disable_labels else "remaining amount: "
    label_paid_amount = "" if disable_labels else "paid amount: "
    label_balance_amount = "" if disable_labels else "balance amount: "
    label_interest = "" if disable_labels else "interest amount: "
    label_balance_sum = "" if disable_labels else "balance sum: "
    label_interest_sum = "" if disable_labels else "interest sum: "
    separator = "\t"  # ", "

    n_months = n_years * 12
    interest_rate = interest_rate_percents / 100
    monthly_interest = interest_rate / 12
    paid_amount = 0

    interest_sum = 0
    balance_sum = 0

    i = 1
    while i <= n_months:
        interest = monthly_interest * amount
        balance_amount = monthly_payment
        balance_amount = balance_amount - interest
        amount = amount - balance_amount
        paid_amount = paid_amount + monthly_payment
        balance_sum = balance_sum + balance_amount
        interest_sum = interest_sum + interest

        print(
            label_month + str(i) + separator + label_remaining_amount + round_str(amount) +
            separator + label_paid_amount + round_str(paid_amount) +
            separator + label_balance_amount + round_str(balance_amount) +
            separator + label_interest + round_str(interest) +
            separator + label_balance_sum + round_str(balance_sum) +
            separator + label_interest_sum + round_str(interest_sum)
        )
        i = i + 1

        if amount - monthly_payment <= 0:
            break

        if amount > extra_payment > 0 == i % 12 and i > 1:
            paid_amount = paid_amount + extra_payment
            amount = amount - extra_payment
            balance_sum = balance_sum + extra_payment


def calculate_monthly_payment(amount, interest_rate_percents, n_years):
    n_months = n_years * 12
    interest_rate = interest_rate_percents / 100
    monthly_interest = interest_rate / 12
    expr1 = math.pow((1 + monthly_interest), -n_months)
    return amount * (monthly_interest / (1 - expr1))


def execute():
    amount = 2712000
    interest_rate = 1.89
    n_years = 20
    monthly_payment = calculate_monthly_payment(amount, interest_rate, n_years)
    print("Monthly payment: " + round_str(monthly_payment))

    payments(amount, interest_rate, n_years, monthly_payment, 0)


def main():
    execute()


if __name__ == "__main__":
    main()
