a = ["C_1","C_5","B_5","D_7","C_9","B_40","C_38","C_37","B_30","B_21","B_25"]

def mergeSort(a):
    if len(a)> 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        #print("Value of L is", L)
        #print("Value of R is", R)
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if int(L[i].split("_")[1]) < int(R[j].split("_")[1]):
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

        #print(a)

mergeSort(a)
print(a)