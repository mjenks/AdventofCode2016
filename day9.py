# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 12:06:18 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = puzzle_input.strip()
    
    return data

def solve(puzzle_data):
    i = 0
    decompressed = ''
    while i < len(puzzle_data):
        char = puzzle_data[i]
        if char == '(':
            i += 1
            marker = puzzle_data[i:].split(')')[0]
            vals = marker.split('x')
            a = int(vals[0]) #num of chars
            b = int(vals[1]) #times repeated
            marker_len = len(marker) + 1
            i += marker_len
            for n in range(b):
                decompressed += puzzle_data[i:i+a]
            i += a
        else:
            decompressed += char
            i += 1
    
    return len(decompressed),0
    
puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
