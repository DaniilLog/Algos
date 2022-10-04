def func(values: list):
    halfSumElem = sum(values) // 2
    first = list()
    second = list()
    for value in values:
        if (sum(first) + value) <= halfSumElem:
            first.append(value)
        else:
            second.append(value)
    if sum(first) == sum(second) == halfSumElem:
        return len(second), second
    else:
        return -1

with open("input.txt","r") as f:
    n = f.readline()
    values = list(map(int,f.readline().split()))
foo = func(values)
with open("output.txt","w") as f:
    if foo != -1:
        length,array = foo[0],foo[1]
        f.write(f"{length}\n{' '.join(map(str,array))}")
    else:
        f.write(str(foo))
