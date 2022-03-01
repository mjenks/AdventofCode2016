# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 12:06:18 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = puzzle_input.strip()
    
    return data
    
def decompress(string):
    i = 0
    decompressed = ''
    while i < len(string):
        char = string[i]
        if char == '(':
            i += 1
            marker = string[i:].split(')')[0]
            vals = marker.split('x')
            a = int(vals[0]) #num of chars
            b = int(vals[1]) #times repeated
            marker_len = len(marker) + 1
            i += marker_len
            for n in range(b):
                decompressed += string[i:i+a]
            i += a
        else:
            decompressed += char
            i += 1
    return decompressed

def solve(puzzle_data):
    first = decompress(puzzle_data)
    weight = [1 for x in puzzle_data]
    index = 0
    length = 0
    while index < len(puzzle_data):
        char = puzzle_data[index]
        if char == '(':
            index +=1
            marker = puzzle_data[index:].split(')')[0]
            vals = marker.split('x')
            a = int(vals[0]) #num of chars
            b = int(vals[1]) #multiplier
            marker_len = len(marker) + 1
            index += marker_len
            for n in range(a):
                if n+index < len(weight):
                    weight[n+index] = b*weight[n+index]
        else:
            length += weight[index]
            index += 1
        
    
    
    return len(first), length
    
puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
