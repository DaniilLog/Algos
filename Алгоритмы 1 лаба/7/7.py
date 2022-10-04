def counter(array, time):
    array.sort()
    count = 0
    for i in array:
        if time < i:
            break
        time -= i
        count += 1
    return count

with open("input.txt","r") as f:
    time,n = list(map(int,f.readline().split()))
    array = list(map(int,f.readline().split()))
with open("output.txt","w") as f:
    f.write(str(counter(array,time)))
