import numpy as np

def re_arrange(list):
    list1 = []
    for i in range(0,len(list)):
        j = np.where(list == i)[0]
        if len(j) !=0:
            list1.append(i)
        else:
            list1.append(-1)

    return list1

list = np.array([3,6,4,1,8,5])
list1 = re_arrange(list)