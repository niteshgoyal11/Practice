a = [1,2,4,5,6,7,8,9,10]

# Find missing number from the sequence using binary search algorithm

def binary_search(a):
    print(a)
    mid = len(a) // 2
    if mid == 0:
        #print(a[0] + 1)
        return (a[0] + 1)
    if a[mid] ==  mid + a[0]:
        print("entered here")
        if len(a) == 2:
            return "No missing elements"
        return (binary_search(a[mid:]))
    else:
        print("I am in else")
        if len(a) == 2:
            if a[1] == a[0] + 1:
                return "No Missing elemetns in else"
            return (a[0] + 1)
        return (binary_search(a[:mid+1]))

print(binary_search(a))