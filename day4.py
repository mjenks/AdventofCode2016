# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:41:41 2022

@author: mjenks
"""

import collections

def parse(puzzle_input):
    data = []
    for room in puzzle_input:
        room = room.strip()
        name = room.split('-')[:-1]
        id_check = room.split('-')[-1]
        sector_id = id_check.split('[')[0]
        checksum = id_check.split('[')[1]
        checksum = checksum[:-1]
        data.append((name, sector_id, checksum))
    return data
   
def isReal(room):
    name, sector, check = room
    name = ''.join(name)
    letter_count = collections.Counter(name)
    c = 0
    samecount = []
    checksum = []
    for letter, count in letter_count.most_common(26):
        if count < c:
            same = sorted(samecount)
            for l in same:
                checksum.append(l)
            samecount = []
        
        samecount.append(letter)
        c = count
    same = sorted(samecount)
    for l in same:
        checksum.append(l)
    checksum = ''.join(checksum)   
       
    if check == checksum[:5]:
        return True
    else:
        return False
    
   
def solve(puzzle_data):
    sector_sum = 0
    valid_rooms = 0
    
    for room in puzzle_data:
        if isReal(room):
            sector_sum += int(room[1])
            valid_rooms += 1
    

    return sector_sum,0

puzzle_path = "input_day4.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
