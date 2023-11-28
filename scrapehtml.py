#!/bin/python3

from bs4 import BeautifulSoup
import requests
import statistics

with open("./index.html", encoding="utf-8", mode="r") as f:
    soup = BeautifulSoup(f, "html.parser")

data = soup.find_all('td')
data.reverse()
del data[1::2]

new_list = []
for color in data:
    new_list.append(color.text)
final_list = []
for color in new_list:
    colors = color.split(',')
    for data in colors:
        final_list.append(data.strip())
print(final_list)

def most_frequent(my_list):
    highest_freq = my_list[0]
    counter = 0

    for item in my_list:
        freq = my_list.count(item)
        if freq > counter:
            counter = freq
            highest_freq = item

    return highest_freq

mostly_worn = most_frequent(final_list)
print(f"The mostly worn color is {mostly_worn}")

def median(my_list):
    """Finds the median of the colors"""
    return statistics.median(my_list)

median_color = median(final_list)
print(f"median_color is {median_color}")

def mean(my_list):
    """computes the mean of the color list"""
    freq = my_list[0]
    counter = 0

    my_dict = {item: my_list.count(item) for item in set(my_list)}
    for key, value in my_dict.items():
        if value > counter:
            counter = value
            freq = key
    return freq

print(f"mean_color is {mean(final_list)}")

for item in final_list:
    if item == "RED":
        no_of_red = final_list.count(item)
probability_red = no_of_red / len(final_list)
print(f"The probability that a color chose at random is red is {probability_red}")