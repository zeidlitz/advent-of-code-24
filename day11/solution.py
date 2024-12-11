import sys
import re
import heapq
from collections import defaultdict, Counter, deque
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
infile = "input.txt"
p1 = 0
p2 = 0
D = open(infile).read().strip()
D = [int(x) for x in D.split()]

DP = {}
def evalueate_stone(x, t):
    if (x,t) in DP:
        return DP[(x,t)]
    if stone == 0:
        ret = 1
    elif x==0:
        ret = evalueate_stone(1, t-1)
    elif len(str(x))%2==0:
        dstr = str(x)
        left = dstr[:len(dstr)//2]
        right = dstr[len(dstr)//2:]
        left, right = (int(left), int(right))
        ret = evalueate_stone(left, t-1) + solve(right, t-1)
    else:
        ret = evalueate_stone(x*2024, t-1)
    DP[(x,t)] = ret
    return ret

def evalueate_stone_all(t):
    return sum(evalueate_stone(x, t) for x in D)

pr(evalueate_stone_all(25))
pr(evalueate_stone_all(75))
