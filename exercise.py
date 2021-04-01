#House Price = 30000
#if buyer has good credit = 10% downpayment
#Otherwise = 28% downpayment

price = 300000
good_credit = False
if good_credit:
    down = (0.1 * 300000)
else:
    down = (0.28 * 300000)

print(f"Payment is RM{down}")