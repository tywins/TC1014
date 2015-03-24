def find_threes(m):
    sum = 0
    for p in m:
        if(p % 3 == 0):
            sum = sum + p
    return sum

n = [0,6,33,8,9,4,3,12]
print(find_threes(n))
