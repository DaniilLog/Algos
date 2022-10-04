def max_income(array_1, array_2):
    maximum = 0
    for i in range(len(array_1)):
        maximum += array_1[i] * array_2[i]
    return maximum

with open("input.txt","r") as f:
    n = int(f.readline())
    a = list(map(int,f.readline().split()))
    b = list(map(int,f.readline().split()))

with open("output.txt","w") as f:
    f.write(str(max_income(sorted(a),sorted(b))))