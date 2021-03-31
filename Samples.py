"""
# Arrays and strings:
By Siavash Hakim Elahi

"""
# Ex1: unique characters
def uniq_ch_finder(str):
    a = list(set(str))
    dd = len(str) - len(a)
    return dd==0


def uniq_ch_finder2(str):
    count = 0
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                count = count + 1
    return count !=0


# Ex2: Permutation
def permutation_string(str1,str2):
    count  = 0
    if len(str1)>len(str2):
        strb = str1
        strs = str2
    else:
        strs = str1
        strb = str2

        for i in range(0,len(strb)-len(strs)+1):
            # print(i)
            # print(strb[i:len(strs)+i] )
            if strb[i:len(strs)+i] == strs:
                count = count + 1
    return count


# Ex2: Permutation method 2
# permutation_string2('god','dog')
def permutation_string2(str1,str2):
    str11 = sorted(str1)
    str22 = sorted(str2)
    return str11 == str22


