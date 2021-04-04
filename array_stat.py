def stat_(list,k):
    list.sort()
    return list[k-1]

list = [2,6,3,9,4,9,1]
print(stat_(list,4))

# O(nlog(n))