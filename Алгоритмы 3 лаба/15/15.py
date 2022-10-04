from collections import deque 
from math import inf 

with open('input.txt', 'r') as f: 
    n, m = map(int, f.readline().split()) 
    garden = [] 
    distance = [] 
    for i in range(n): 
        garden.append(list(f.readline().strip('\n'))) 
        distance.append([inf] * m) 
    qx, qy, L = map(int, f.readline().split()) 
    qx -= 1 
    qy -= 1 
    knights = [] 
    for i in range(4): 
        x, y, p = map(int, f.readline().split()) 
        knights.append((x, y, p)) 
 
steps = [(0, 1), (1, 0), (-1, 0), (0, -1)] 
distance[qx][qy] = 0 
 
queue = deque() 
 
queue += [[qx, qy]] 
 
while len(queue): 
    vx, vy = queue.popleft() 
    for step in steps: 
        x = vx + step[0] 
        y = vy + step[1] 
        if garden[x][y] == '0' and distance[x][y] == inf: 
            queue += [[x, y]] 
            distance[x][y] = distance[vx][vy] + 1 
 
count = 0 
 
for k in knights: 
    if 0 <= distance[k[0] - 1][k[1] - 1] <= L: 
        count += k[2] 
with open('output.txt', 'w') as f: 
    f.write(str(count))