"""
File: can_sizes.py
Authors: David Mendenhall, Miles Noble, Spencer Sowby

Purpose:
    Work as a team to write a Python program named can_sizes.py that computes and prints
    the storage efficiency for each of the following 12 steel can sizes.
    Then visually examine the output and answer this question,
    "Which can size has the highest storage efficiency?"

    If you separate your program into functions, this problem will be much easier to solve
    than if you don't separate it into functions. You are free to write any functions that
    you choose in your program, but we strongly suggest that your program include at least
    these three functions:

    Core Requirements
        1. Your program must compute the volume of all 12 can sizes.
        2. Your program must compute the surface area of all 12 can sizes.
        3. Your program must compute and print the storage efficiency of all 12 can sizes.

    Stretch Challenges
        1. Add another function named compute_storage_efficiency to your program. This function
        should call the compute_volume and compute_surface_area functions and then compute and
        return the storage efficiency of a steel can size. Replace code in the main function
        with a call to the compute_storage_efficiency function as appropriate. Did adding and
        calling the compute_storage_efficiency function reduce the number of lines of code in
        your program?

        2. The table of can sizes that appears in the Assignment section above includes a column
        that contains the cost per can of each steel can size. Add another function to your program
        named compute_cost_efficiency that computes and returns the volume of a steel can divided
        by its cost. Write code to call the compute_cost_efficiency function and print the cost
        efficiency for each can size. Then visually examine the output and answer this question,
        "Which can size has the highest cost efficiency?"

        3. If you remember how to use lists and a for loop from CSE 110, rewrite your main function
        so that it uses a list or lists that contain the can size names and dimensions. Then write
        a loop that processes the values in the list.

        4. Add if statements inside the loop to automatically determine which can size has the
        best storage efficiency and which can size has the best cost efficiency.
"""

import math


all_cans = [
    ["#1 Picnic", 6.83, 10.16, 0.28],
    ["#1 Tall", 7.78, 11.91, 0.43],
    ["#2", 8.73, 11.59, 0.45],
    ["#2.5", 10.32, 11.91, 0.61],
    ["#3 Cylinder", 10.79, 17.78, 0.86],
    ["#5", 13.02, 14.29, 0.83],
    ["#6Z", 5.40, 8.89, 0.22],
    ["#8Z short", 6.83, 7.62, 0.26],
    ["#10", 15.72, 17.78, 1.53],
    ["#211", 6.83, 12.38, 0.34],
    ["#300", 7.62, 11.27, 0.38],
    ["#303", 8.10, 11.11, 0.42]
]


def main():
    best_cost = 0
    best_eff = 0
    best_eff_i = ""
    best_cost_i = ""
    for i in range(len(all_cans)):
        efficiency = compute_storage_efficiency(all_cans[i][1], all_cans[i][2])
        cost_efficiency = compute_cost_efficiency(
            all_cans[i][1], all_cans[i][2], all_cans[i][3])
        print(
            f"{all_cans[i][0]:<15}{round(efficiency, 2):<10.2f}{round(cost_efficiency, 2):.2f} cm^3 per $")

        if efficiency > best_eff:
            best_eff = efficiency
            best_eff_i = all_cans[i][0]

        if cost_efficiency > best_cost:
            best_cost = cost_efficiency
            best_cost_i = all_cans[i][0]

    print(
        f"\nBest Storage Efficiency: {best_eff_i} with: {round(best_eff, 2):.2f}")
    print(
        f"Best Cost Efficiency: {best_cost_i} with: {round(best_cost, 2):.2f}")


def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(radius, height):
    efficiency = compute_volume(radius, height) / \
        compute_surface_area(radius, height)
    return efficiency


def compute_cost_efficiency(radius, height, cost):
    cost_efficiency = compute_volume(radius, height) / cost
    return cost_efficiency


main()
