# TechnicalTests
Python scripts

Run with:
> python .\techtest1.py
> 
> python .\techtest2.py

## 1. Python script that calculates a path of stones and a frog, that wants to jump from the first to the last stone and returns back. The path is provided as an integer array starting with 0, each stone element has an unique value and the array is sorted in increasing order. 
for example: stones_path = [0,3,8,15,20]

Important conditions are: 
The frog can jump on each stone only once.
The frog starts jumping from the first stone to the last one and then comes back to the first stone again.
The length of each jump is the absolute value difference between the values of the stones which the frog jumps on. For example, if the frog is at stones_path[i] and is jumping to stones_path[j], the length of the jump is |stones[i] - stones[j]|.
The cost of a path is the maximum length of a jump among all jumps in the path.
Return the minimum possible cost of a path for the frog.

Constraints:
2 <= len(stones_path) <= 100
stones_path[0] == 0
stones_path is sorted in a strictly increasing order.

## 2. Python program that:
    a. Opens the following webpage: https://en.wikipedia.org/wiki/ASEAN
    b. Extracts the data_rows from the 'Urban areas' table (Demographics section) on that page.
    c. Using values from columns 'Country', 'Core City', and 'Population' it should create a countries_dictionary variable with a valid json containing country, All respective cities in given country, their population and area.
    d. Calculate population density for all countries and metropolitan areas in the dictionary and add in to the countries_dictionary. Print the content.
    e. Saves the information to a file
    f. upon each script run it should compare the latest data with the one saved in the file before and it should rewrite the file only if there is new data.
