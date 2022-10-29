"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# Ask the user for their age
age = int(input("Please enter your age: "))

# Find the max heart rate per minute
max = 220 - age

# Find the low heart rate range
low = max * .65

# Find the high heart rate range
high = max * .85

print("When you exercise to strengthen your heart, ")
print(f"you should keep you heart rate between {low:.0f} and {high:.0f} beats per minutes.")