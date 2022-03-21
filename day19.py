# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:07:25 2022

@author: mjenks
"""
import math

def find_power(num):
    power = 0
    while num//2 != 0:
        power += 1
        num = num//2
    return power
    
def solve(puzzle_data):
    #part one is odd number that would be refrenced by the index (in a list of odds) of the remaining value after removing the nearest power of 2
    #find the nearest power of 2
    power = find_power(puzzle_data)
    remaining = puzzle_data - math.pow(2, power)
            

    return remaining*2 + 1, 0

    
puzzle_data = 3014387
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)