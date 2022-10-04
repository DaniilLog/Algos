dict = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [6, 2], 8: [1, 3], 9: [2, 4]}
startCount = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0, 9: 1}
endCount = {}
with open("input.txt","r") as f:
    length = int(f.readline())
for i in range(length - 1):
    for key in dict:
        sum = 0
        for j in dict[key]:
            sum += startCount[j]
        endCount[key] = sum
    startCount = endCount
    endCount = {}
sum = 0
for key in startCount:
    sum += startCount[key]

with open("output.txt","w") as f:
    f.write(str(sum % (10 ** 9)))

