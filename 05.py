def sumL(l2):
    if len(l2) != 0:
        return l2[0] + sumL(l2[1:])
    return 0

def maxL(l2,maxim):
    if len(l2) != 0:
        if l2[0] >= maxim:
            return maxL(l2[1:], l2[0])
        return maxL(l2[1:], maxim)
    return maxim

def minL(l2,minum):
    if len(l2) != 0:
        if l2[0] <= minum:
            return minL(l2[1:], l2[0])
        return minL(l2[1:], minum)
    return minum

l2 = [1, 3, 7, 9, 2, 7]
maxim = 0
minum = maxL(l2,maxim)

print(sumL(l2))
print(maxL(l2,maxim))
print(minL(l2,minum))
