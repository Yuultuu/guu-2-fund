def sumL(l2, suml):
    if len(l2) == 0:
        return suml
    suml1 = l2[0] + suml
    return sumL(l2[1:], suml1)

def maxL(l2,maxim):
    if len(l2) == 0:
        return maxim
    if l2[0] >= maxim:
        return maxL(l2[1:], l2[0])
    return maxL(l2[1:], maxim)

def minL(l2,minum):
    if len(l2) == 0:
        return minum
    if l2[0] <= minum:
        return minL(l2[1:], l2[0])
    return minL(l2[1:], minum)

l2 = [1, 3, 7, 9, 2, 7]
maxim = 0
suml = 0
minum = min(l2)