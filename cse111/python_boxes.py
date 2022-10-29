# 02 Checkpoint: Calling Functions

import math

# Get the number of manufactured items
number_of_items = float(input("Enter the number of items: "))

# Get the number of items that the user will pack per box
items_per_box = float(input("Enter the number of items per box: "))

# Call the math.ceil function and store its return value in a variable to use later
number_of_boxes = (math.ceil(number_of_items / items_per_box))

print(f"For {number_of_items:.0f} items, packing {items_per_box:.0f} items in each box, you will need {number_of_boxes:.0f} boxes. ")
