with open("input.txt", "r") as f: 
    n, k = map(int, f.readline().split()) 
    string = f.read() 

pali = [[0 for i in range(n)] for j in range(n)] 
for l in range(n + 1, -1, -1): 
    for r in range(1, n): 
        if r > l: 
            pali[l][r] = pali[l + 1][r - 1] if string[l] == string[r] else pali[l + 1][r - 1] + 1 

for line in pali: 
    print(line) 

el_to_swap = 0 
for l_board in range(n): 
    for r_board in range(l_board, n): 
        if pali[l_board][r_board] <= k: 
            el_to_swap += 1 

with open("output.txt", "w") as f: 
    f.write(str(el_to_swap))