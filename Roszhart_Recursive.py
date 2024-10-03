def findMin(l):
    if l == []:
        return Null
    else:
        return findMin2(l, l[0])

def findMin2(l, min):
    if l == []:
        return min
    if l[0] < min:
        min = l[0]
    return findMin2(l[1:], min)

def findMax(l):
    if l == []:
        return Null
    else:
        return findMax2(l, l[0])
    
def findMax2(l, max):
    if l == []:
        return max
    if l[0] > max:
        max = l[0]
    return findMax2(l[1:], max)

print(findMin([5,2,6,1,9]))
print(findMax([5,2,6,1,9]))