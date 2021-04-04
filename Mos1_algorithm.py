def Mo(list,q_range):
    sum = 0
    for i in range(q_range[0],q_range[1]):
        sum = sum + list[i]

    return sum

list = [2,6,3,9,4,9,1]
print(Mo(list,[1,3]))

