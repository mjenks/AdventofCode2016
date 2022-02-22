# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 20:57:25 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(list(line.strip()))

    return data

def find_button(key, code):
    for inst in code:
        if inst == 'U' and key[0] > 1:
            key = (key[0] - 1, key[1])
        elif inst == 'D' and key[0] < 3:
            key = (key[0] + 1, key[1])
        elif inst == 'L' and key[1] > 1:
            key = (key[0], key[1] -1)
        elif inst == 'R' and key[1] < 3:
            key = (key[0], key[1] + 1)
    
    return key
    
def find_button2(key, code):
    for inst in code:
        if inst == 'U' and key[0] > 1:
            if key[1] <= 3 and sum(key) > 4:
                key = (key[0] - 1, key[1])
            elif key[1] > 3:
                if key != (2,4) and key != (3,5):
                    key = (key[0] - 1, key[1])
        elif inst == 'D' and key[0] < 5:
            if key[1] >= 3 and sum(key) < 8:
                key = (key[0] + 1, key[1])
            elif key[1] < 3:
                if key != (3, 1) and key != (4,2):
                    key = (key[0] + 1, key[1])
        elif inst == 'L' and key[1] > 1:
            if key[0] <= 3 and sum(key) > 4:
                key = (key[0], key[1] -1)
            elif key[0] > 3:
                if key != (4,2) and key != (5,3):
                   key = (key[0], key[1] -1) 
        elif inst == 'R' and key[1] < 5:
            if key[0] >= 3 and sum(key) < 8:
                key = (key[0], key[1] + 1)
            elif key[0] < 3:
                if key != (1, 3) and key != (2,4):
                    key = (key[0], key[1] + 1)
    
    return key

def solve(puzzle_data):
    key = (2, 2) #define key locations by row column
    key2 = (3, 1)
    buttons = []
    buttons2 = []
    code = []
    code2 = []
    
    for line in puzzle_data:
        key = find_button(key, line)
        buttons.append(key)
        
    #convert the button location into number values
    for button in buttons:
        if button[0] == 1:
            if button[1] == 1:
                code.append(1)
            elif button[1] == 2:
                code.append(2)
            elif button[1] == 3:
                code.append(3)
        elif button[0] == 2:
            if button[1] == 1:
                code.append(4)
            elif button[1] == 2:
                code.append(5)
            elif button[1] == 3:
                code.append(6)
        elif button[0] == 3:
            if button[1] == 1:
                code.append(7)
            elif button[1] == 2:
                code.append(8)
            elif button[1] == 3:
                code.append(9)
                
    for line in puzzle_data:
        key2 = find_button2(key2, line)
        buttons2.append(key2)
        
    #convert the button location into number values
    for button in buttons2:
        if button[0] == 1:
            if button[1] == 3:
                code2.append(1)
        elif button[0] == 2:
            if button[1] == 2:
                code2.append(2)
            elif button[1] == 3:
                code2.append(3)
            elif button[1] == 4:
                code2.append(4)
        elif button[0] == 3:
            if button[1] == 1:
                code2.append(5)
            elif button[1] == 2:
                code2.append(6)
            elif button[1] == 3:
                code2.append(7)
            elif button[1] == 4:
                code2.append(8)
            elif button[1] == 5:
                code2.append(9)
        elif button[0] == 4:
            if button[1] == 2:
                code2.append('A')
            elif button[1] == 3:
                code2.append('B')
            elif button[1] == 4:
                code2.append('C')
        elif button[0] == 5:
            if button[1] == 3:
                code2.append('D')
    
    return code, code2

puzzle_path = "input_day2.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)
#solution1, solution2 = solve([['U', 'L', 'L'], ['R', 'R', 'D', 'D', 'D']])

print(solution1)
print(solution2)