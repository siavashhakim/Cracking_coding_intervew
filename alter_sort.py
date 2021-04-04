def alter_sort(list):
    list.sort()
    output = []
    for i in range(0,int(len(list)/2)):
        output.append(list[len(list)-i-1])
        output.append(list[i])

    return output


list = [4,3,5,4,1,2,9]
print(alter_sort(list))