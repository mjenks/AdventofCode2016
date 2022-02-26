# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:52:17 2022

@author: mjenks
"""

import collections

def parse(puzzle_input):
    #8 letter word
    ltr1 = []
    ltr2 = []
    ltr3 = []
    ltr4 = []
    ltr5 = []
    ltr6 = []
    ltr7 = []
    ltr8 = []
    for msg in puzzle_input:
        ltr1.append(msg[0])
        ltr2.append(msg[1])
        ltr3.append(msg[2])
        ltr4.append(msg[3])
        ltr5.append(msg[4])
        ltr6.append(msg[5])
        ltr7.append(msg[6])
        ltr8.append(msg[7])
        
    data = [ltr1, ltr2, ltr3, ltr4, ltr5, ltr6, ltr7, ltr8]    
    return data
    
def solve(puzzle_data):
    message1 = []
    message2 = []
    for letter in puzzle_data:
        count = collections.Counter(letter).most_common()
        most = count[0]
        least = count[-1]
        message1.append(most[0])
        message2.append(least[0])
        
    return ''.join(message1), ''.join(message2)
    
puzzle_path = "input_day6.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)