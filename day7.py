# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:21:06 2022

@author: mjenks
"""
def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(line.strip())
        
    return data
    
def tls_supported(ip):
    ip = list(ip)
    bracketed = False
    supported = False
    l1 = ip[0]
    l2 = ip[1]
    l3 = ip[2]
    for letter in ip[3:]:
        if letter == '[':
            l1 = ''
            l2 = ''
            l3 = ''
            l4 = ''
            bracketed = True
        elif letter == ']':
            l1 = ''
            l2 = ''
            l3 = ''
            l4 = ''
            bracketed = False
        else:
            l4 = letter
            #test for abba sequence
            if l1 == l4 and l2 == l3 and l1 != l2:
                if bracketed:
                    supported = False
                    break
                else:
                    supported = True
            l1 = l2
            l2 = l3
            l3 = l4
            
    return supported

def ssl_supported(ip):
    supported = False
    supernet = []
    hypernet = []
    for part in ip.split('['):
        if ']' in part:
            hypernet.append(part.split(']')[0])
            supernet.append(part.split(']')[1])
        else:
            supernet.append(part)
    aba = []
    for part in supernet:
        seq = list(part)
        l1 = seq[0]
        l2 = seq[1]
        for letter in seq[2:]:
            l3 = letter
            if l1 == l3 and l2 != l1:
                aba.append(l1+l2+l3)
            l1 = l2
            l2 = l3
    hypernet = ' '.join(hypernet)
    for seq in aba:
        bab = seq[1] + seq[0] + seq[1]
        if bab in hypernet:
            supported = True
                
    return supported
    
def solve(puzzle_input):
    tls_count = 0
    ssl_count = 0
    for ip in puzzle_input:
        if tls_supported(ip):
            tls_count += 1
        if ssl_supported(ip):
            ssl_count += 1
    return tls_count, ssl_count

puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)