# Python3 program for rearrange an
# array such that arr[i] = i.

# Function to rearrange an array
# such that arr[i] = i.
def fix(arr):
    n = len(arr)
    i = 0
    while i < n:

        if (arr[i] >= 0 and arr[i] != i):
            (arr[arr[i]],
             arr[i]) = (arr[i],
                        arr[arr[i]])
        else:
            i += 1

    return arr

# Driver code
if __name__ == "__main__":
    A = [0,6, 1, 9,3, 2,  4,]
    print(fix(A))