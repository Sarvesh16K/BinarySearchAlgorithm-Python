l = list(map(int,input("Enter elements of lists seperated by space: ").split()))
target = int(input("Enter target: "))
l.sort()
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high<low:
        return -1
    mid = (low + high) // 2
    if(l[mid]==target):
        return mid
    elif(l[mid]>target):
        return binary_search(l, target, low, mid-1)
    else:
        return binary_search(l, target, mid+1, high)
print(l)
print("Index of",target,"in sorted list is",binary_search(l,target))