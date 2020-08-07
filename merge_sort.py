a = [1,5,3,7,9,40,38,37,30,21,25]

def mergeSort(a):
    if len(a)> 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        print("Value of L is", L)
        print("Value of R is", R)
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        while (i < len(L)):
            a[k] = L[i]
            i += 1
            k += 1

        while (j < len(R)):
            a[k] = R[j]
            j += 1
            k += 1

        print(a)

mergeSort(a)
print(a)