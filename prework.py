customer_name = input("Enter your name in the field:" )
purchase_total = float(input("Type your purchase total here:" ))
shipping_total = 12.00

#free shipping with a purchase of $50 or more. A specialized message prints at different purchase totals. 
if purchase_total >= 50.00:
    shipping_toal = 0.00
    print(customer_name + ", hooray! You qualify for free shipping and this month's freebie with your $" + str(purchase_total) + " purchase!")
elif purchase_total == 35.00:
    shipping_toal = 12.00
    print(customer_name + ", you're so close! Spend $50 or more and get free shipping plus this month's freebie.")
else: 
    print(customer_name + ", thank you for your purchase.")

