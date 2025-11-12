def total_calc(bill, tip):
    total = bill*(1+0.01 * tip)
    total = round(total, 2)
    return total


print(total_calc(100,20))
