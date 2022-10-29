import math
from datetime import datetime
from tkinter.messagebox import NO, YES

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi*w**2*a*(w*a + 2540*d)/10000000000

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:

    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume: .2f}",
          file=volumes_file)
    # old print statement = print(f"The approximate volume is {volume: .2f} liters", file=volumes_file)

purchase = str(
    input("Did you want to buy the tires with the dimensions you entered?: "))

if purchase == YES:
    phone_number = str(
        input("What is the best phone number to have on file for you? "))

    with open("volumes.txt", "at") as volumes_file:
        print(f"{phone_number}", file=volumes_file)

else:
    pass
