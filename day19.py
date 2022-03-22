# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:07:25 2022

@author: mjenks
"""
import math

def findElf(num):
    elves = range(1,num+1)
    i = 0
    while len(elves) > 1:
        num = len(elves)
        elf = elves[i]
        out = elves[(i + num//2)%num]
        elves.remove(elves[(i + num//2)%num])
        if out > elf:
            i = (i+1)%len(elves)
        else:
            i = i%len(elves)
        
    return elves[0]

def find_power(num, base):
    power = 0
    while num//base != 0:
        power += 1
        num = num//base
    return power
    
def solve(puzzle_data):
    #part one is odd number that would be refrenced by the index (in a list of odds) of the remaining value after removing the nearest power of 2
    #find the nearest power of 2
    power = find_power(puzzle_data, 2)
    remaining = puzzle_data - math.pow(2, power)
    
    #part 2 pattern found using the findElf function        
    #part 2 the pattern is starting at 1 each piece is every value to that previous highest then continue that many odd numbers
    # the final values for each pattern segment are 1,3,9,27,81,... powers of 3
    # and occurs at the corresponding number of elves 3 elves is elf 3 27 elves is 27 ect
    power2 = find_power(puzzle_data, 3)
    if 2*math.pow(3,power2) >= puzzle_data: #it is in the normal counting part
        part2 = puzzle_data - math.pow(3,power2)
    else: #in the odds part
        part2 = math.pow(3,power2) + 2*(puzzle_data - 2*math.pow(3,power2))

    return remaining*2 + 1, part2

    
puzzle_data = 3014387
solution1, solution2 = solve(puzzle_data)


print(solution1)
print(solution2)