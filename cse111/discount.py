"""
Get a customer's subtotal as input and gets the current day of the week from your computer's operating system.
Your program must not ask the user to enter the day of the week. Instead, it must get the day of the week from your
computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal.
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print
the discount amount if applicable, the sales tax amount, and the total amount due.

Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your
computer's operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.

Stretch Challenges
If your team finishes the core requirements in less than an hour, complete one or more of these stretch challenges. Note that the stretch challenges

Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing enough to receive the
discount. This added code should compute and print the difference between $50 and the subtotal which is the additional amount the customer would need
to purchase in order to receive the discount.

Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a
quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.
"""

from calendar import weekday
from datetime import datetime

day = datetime.now().weekday()
subtotal = 0
price = -1

price = float(input("What is the price of the item: "))
while price != 0:
    quantity = float(input("How many items: "))
    subtotal = float(price * quantity)
    price = float(input("What is the price of the item: "))

print(f"Subtotal: ${subtotal:.2f}")
if subtotal >= 50 and (day == 1 or day == 2):
    discount = round(subtotal * 0.10, 2)
    print(f"Discount amount: ${discount:.2f}")
    subtotal -= discount
elif subtotal < 50:
    difference = 50 - subtotal
    print(f"You need to spend ${difference:.2f} more to get a 10% discount.")

sales_tax = round(subtotal * 0.06, 2)
print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total: ${subtotal + sales_tax:.2f}")
