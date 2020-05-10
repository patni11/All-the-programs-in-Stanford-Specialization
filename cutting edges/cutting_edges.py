import numpy as np
import random
import copy

time = 0
f = open('question.txt','r')
Graph = {}
for line in f:
    Graph[int(line.split()[0])] = [int(j) for j in line.split()[1:]]
#print(Graph)
def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def contract(G):
    global time
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1) 
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    print(time)
    time += 1
    return length[0]



def krager(n,G):
    count = 10000
    for i in range(n):
        graph = copy.deepcopy(G)
        min_val = contract(graph)
        if min_val < count:
            count = min_val
    return count

print(krager(250,Graph))        