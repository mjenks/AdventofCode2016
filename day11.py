# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 20:21:38 2022

@author: mjenks
"""

steps_needed = []

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(',')
        chips = set()
        rtgs = set()
        for item in line:
            item = item.split()
            if 'chip' in item[-1]:
                chips.add(item[-2][:-11])
            if 'generator' in item[-1]:
                rtgs.add(item[-2])
        data.append((chips, rtgs))
        
    return data
    
def check(floor):
    fried = False
    if len(floor[1]) != 0:
        for chip in floor[0]:
            if chip not in floor[1]:
                fried = True
    return not fried
        
    
def move(start, prior_states, count):
    global steps_needed
    if len(steps_needed) != 0:
        steps_needed.sort()
        if count >= steps_needed[0]:
            return
            
    #check if solved all 5 chips and rtg on 4th floor
    elevator, floors = start
    floor4 = floors[3]
    if len(floor4[0]) == 5 and len(floor4[1]) == 5:
        steps_needed.append(count)
        return
        
    
    #find and run for all possible moves
    if elevator == 1:
        current = floors[0]
        des = floors[1]
        #try moving 1 or 2 chips up
        for chip1 in current[0]:
            current[0].remove(chip1)
            des[0].add(chip1)
            if check(des):
                new_state = elevator + 1, (current, des, floors[2], floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
                    
            for chip2 in current[0]:
                current[0].remove(chip2)
                des[0].add(chip2)
                if check(des):
                    new_state = elevator + 1, (current, des, floors[2], floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip2)
                des[0].remove(chip2)  
            des[0].remove(chip1)
            current[0].add(chip1)
        #try moving 1 or 2 rtgs
        for rtg1 in current[1]:
            current[1].remove(rtg1)
            des[1].add(rtg1)
            if check(des):
                new_state = elevator + 1, (current, des, floors[2], floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for rtg2 in current[1]:
                current[1].remove(rtg2)
                des[1].add(rtg2)
                if check(des):
                    new_state = elevator + 1, (current, des, floors[2], floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[1].add(rtg2)
                des[1].remove(rtg2)  
            des[1].remove(rtg1)
            current[1].add(rtg1)
        #try moving up a pair
        for chip in current[0]:
            if chip in current[1]:
                current[0].remove(chip)
                current[1].remove(chip)
                des[0].add(chip)
                des[1].add(chip)
                if check(des):
                    new_state = elevator + 1, (current, des, floors[2], floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip)
                current[1].add(chip)
                des[0].remove(chip)
                des[1].remove(chip)

    elif elevator == 2:
        current = floors[1]
        des = floors[2]
        #try moving 1 or 2 chips up
        for chip in current[0]:
            current[0].remove(chip)
            des[0].add(chip)
            if check(des):
                new_state = elevator + 1, (floors[0], current, des, floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for chip2 in current[0]:
                current[0].remove(chip2)
                des[0].add(chip2)
                if check(des):
                    new_state = elevator + 1, (floors[0], current, des, floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip2)
                des[0].remove(chip2)  
            des[0].remove(chip)
            current[0].add(chip)
        #try moving 1 or 2 rtgs
        for rtg in current[1]:
            current[1].remove(rtg)
            des[1].add(rtg)
            if check(des):
                new_state = elevator + 1, (floors[0], current, des, floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for rtg2 in current[1]:
                current[1].remove(rtg2)
                des[1].add(rtg2)
                if check(des):
                    new_state = elevator + 1, (floors[0], current, des, floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[1].add(rtg2)
                des[1].remove(rtg2)  
            des[1].remove(rtg)
            current[1].add(rtg)
        #try moving up a pair
        for chip in current[0]:
            if chip in current[1]:
                current[0].remove(chip)
                current[1].remove(chip)
                des[0].add(chip)
                des[1].add(chip)
                if check(des):
                    new_state = elevator + 1, (floors[0], current, des, floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip)
                current[1].add(chip)
                des[0].remove(chip)
                des[1].remove(chip)
                
        #down
        des = floors[0]
        #try moving 1 or 2 chips down
        for chip in current[0]:
            current[0].remove(chip)
            des[0].add(chip)
            if check(des):
                new_state = elevator + 1, (des, current, floors[2], floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for chip2 in current[0]:
                current[0].remove(chip2)
                des[0].add(chip2)
                if check(des):
                    new_state = elevator + 1, (des, current, floors[2], floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip2)
                des[0].remove(chip2)  
            des[0].remove(chip)
            current[0].add(chip)
        #try moving 1 or 2 rtgs
        for rtg in current[1]:
            current[1].remove(rtg)
            des[1].add(rtg)
            if check(des):
                new_state = elevator + 1, (des, current, floors[2], floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for rtg2 in current[1]:
                current[1].remove(rtg2)
                des[1].add(rtg2)
                if check(des):
                    new_state = elevator + 1, (des, current, floors[2], floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[1].add(rtg2)
                des[1].remove(rtg2)  
            des[1].remove(rtg)
            current[1].add(rtg)
        #try moving up a pair
        for chip in current[0]:
            if chip in current[1]:
                current[0].remove(chip)
                current[1].remove(chip)
                des[0].add(chip)
                des[1].add(chip)
                if check(des):
                    new_state = elevator + 1, (des, current, floors[2], floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip)
                current[1].add(chip)
                des[0].remove(chip)
                des[1].remove(chip)
    elif elevator == 3:
        current = floors[2]
        des = floors[3]
        #try moving 1 or 2 chips up
        for chip in current[0]:
            current[0].remove(chip)
            des[0].add(chip)
            if check(des):
                new_state = elevator + 1, (floors[0], floors[1], current, des)
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for chip2 in current[0]:
                current[0].remove(chip2)
                des[0].add(chip2)
                if check(des):
                    new_state = elevator + 1, (floors[0], floors[1], current, des)
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip2)
                des[0].remove(chip2)  
            des[0].remove(chip)
            current[0].add(chip)
        #try moving 1 or 2 rtgs
        for rtg in current[1]:
            current[1].remove(rtg)
            des[1].add(rtg)
            if check(des):
                new_state = elevator + 1, (floors[0], floors[1], current, des)
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for rtg2 in current[1]:
                current[1].remove(rtg2)
                des[1].add(rtg2)
                if check(des):
                    new_state = elevator + 1, (floors[0], floors[1], current, des)
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[1].add(rtg2)
                des[1].remove(rtg2)  
            des[1].remove(rtg)
            current[1].add(rtg)
        #try moving up a pair
        for chip in current[0]:
            if chip in current[1]:
                current[0].remove(chip)
                current[1].remove(chip)
                des[0].add(chip)
                des[1].add(chip)
                if check(des):
                    new_state = elevator + 1, (floors[0], floors[1], current, des)
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip)
                current[1].add(chip)
                des[0].remove(chip)
                des[1].remove(chip)
                
        #try down
        des = floors[1]
        #try moving 1 or 2 chips down
        for chip in current[0]:
            current[0].remove(chip)
            des[0].add(chip)
            if check(des):
                new_state = elevator + 1, (floors[0], des, current, floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for chip2 in current[0]:
                current[0].remove(chip2)
                des[0].add(chip2)
                if check(des):
                    new_state = elevator + 1, (floors[0], des, current, floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip2)
                des[0].remove(chip2)  
            des[0].remove(chip)
            current[0].add(chip)
        #try moving 1 or 2 rtgs
        for rtg in current[1]:
            current[1].remove(rtg)
            des[1].add(rtg)
            if check(des):
                new_state = elevator + 1, (floors[0], des, current, floors[3])
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for rtg2 in current[1]:
                current[1].remove(rtg2)
                des[1].add(rtg2)
                if check(des):
                    new_state = elevator + 1, (floors[0], des, current, floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[1].add(rtg2)
                des[1].remove(rtg2)  
            des[1].remove(rtg)
            current[1].add(rtg)
        #try moving up a pair
        for chip in current[0]:
            if chip in current[1]:
                current[0].remove(chip)
                current[1].remove(chip)
                des[0].add(chip)
                des[1].add(chip)
                if check(des):
                    new_state = elevator + 1, (floors[0], des, current, floors[3])
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip)
                current[1].add(chip)
                des[0].remove(chip)
                des[1].remove(chip)
    elif elevator == 4:
        current = floors[3]
        des = floors[2]
        #try moving 1 or 2 chips down
        for chip in current[0]:
            current[0].remove(chip)
            des[0].add(chip)
            if check(des):
                new_state = elevator + 1, (floors[0], floors[2], des, current)
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for chip2 in current[0]:
                current[0].remove(chip2)
                des[0].add(chip2)
                if check(des):
                    new_state = elevator + 1, (floors[0], floors[2], des, current)
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip2)
                des[0].remove(chip2)  
            des[0].remove(chip)
            current[0].add(chip)
        #try moving 1 or 2 rtgs
        for rtg in current[1]:
            current[1].remove(rtg)
            des[1].add(rtg)
            if check(des):
                new_state = elevator + 1, (floors[0], floors[2], des, current)
                state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                if state not in prior_states:
                    prior_states.add(state)
                    move(new_state, prior_states, count+1)
                    prior_states.remove(state)
            for rtg2 in current[1]:
                current[1].remove(rtg2)
                des[1].add(rtg2)
                if check(des):
                    new_state = elevator + 1, (floors[0], floors[2], des, current)
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[1].add(rtg2)
                des[1].remove(rtg2)  
            des[1].remove(rtg)
            current[1].add(rtg)
        #try moving up a pair
        for chip in current[0]:
            if chip in current[1]:
                current[0].remove(chip)
                current[1].remove(chip)
                des[0].add(chip)
                des[1].add(chip)
                if check(des):
                    new_state = elevator + 1, (floors[0], floors[2], des, current)
                    state = (elevator, (len(new_state[1][0][0]),len(new_state[1][0][1])), (len(new_state[1][1][0]),len(new_state[1][1][1])), (len(new_state[1][2][0]),len(new_state[1][2][1])), (len(new_state[1][3][0]),len(new_state[1][3][1])))
                    if state not in prior_states:
                        prior_states.add(state)
                        move(new_state, prior_states, count+1)
                        prior_states.remove(state)
                current[0].add(chip)
                current[1].add(chip)
                des[0].remove(chip)
                des[1].remove(chip)
    return
                
    
    
def solve(puzzle_data):
    global steps_needed
    elevator = 1
    start_state = elevator, puzzle_data
    #a set to hold a list of equivelent states that a path has had 
    #elevator location and the number of chips, number of rtgs for each floor
    prior_states = {(elevator, (len(start_state[1][0][0]),len(start_state[1][0][1])), (len(start_state[1][1][0]),len(start_state[1][1][1])), (len(start_state[1][2][0]),len(start_state[1][2][1])), (len(start_state[1][3][0]),len(start_state[1][3][1])))}
    
    move(start_state, prior_states, 0)
    steps_needed.sort()
    return 0

puzzle_path = "input_day11.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution2 = solve(puzzle_data)
solution1 = min(steps_needed, 1000000)

print(solution1)
print(solution2)