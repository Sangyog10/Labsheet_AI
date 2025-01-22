from queue import PriorityQueue
import math
import pprint
G = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25, "Biratchowk": 30},
    "Itahari": {"Biratnagar": 22, "Dharan": 20, "Biratchowk": 11},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Biratnagar": 30, "Itahari": 11, "Kanepokhari": 10},
    "Kanepokhari": {"Biratchowk": 10, "Rangeli": 25, "Urlabari": 12},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25, "Urlabari": 40},
    "Urlabari": {"Kanepokhari": 12, "Rangeli": 40, "Damak": 6},
    "Damak": {"Urlabari": 6},
}

h= {
    "Biratnagar": 46,
    "Itahari": 39,
    "Dharan": 41,
    "Biratchowk": 29,
    "Kanepokhari": 17,
    "Rangeli": 28,
    "Urlabari": 6,
    "Damak": 0
}

def aStar(G, h, start, goal):
    PQ = PriorityQueue()
    prev=dict()
    visited = set()
    PQ.put((0+h[start], (start,0))) #using tuple (fScore,(state,gScore))
    prev[start]=" "
    while(not PQ.empty()):
        outStatefScore, (outState, outstateGScore)= PQ.get()
        visited.add(outState)
        if(outState == goal):
            return True, prev, outstateGScore
        for chimeki in G[outState].keys():
            if chimeki not in visited:
                chimekiGscore=outstateGScore + G[outState][chimeki]
                PQ.put((chimekiGscore+h[chimeki],(chimeki, chimekiGscore)))
                prev[chimeki]= outState
    return False, prev, math.inf

def reconstruct_path(G, prev, goal):
    path = goal
    while prev[goal] != " ":
        path = prev[goal] + "->" + path
        goal= prev[goal]
    return path
        

start = "Dharan"
goal = "Damak"
goalFound, prev, cost = aStar(G, h, start, goal)
if(goalFound):
    print(reconstruct_path(G, prev, goal))
    print("Cost = ", cost)
else:
    print("No solution found")
        
