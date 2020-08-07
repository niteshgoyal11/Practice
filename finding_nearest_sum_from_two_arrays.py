arr1 = [1,10,20,30,40,100]

arr2 = [10,20,31,40,50,60,70,80,90,100]

k = 30

l = 0
r = len(arr2) - 1
arr1_val = arr1[l]
arr2_val = arr2[r]
diff = 99999999
while l < len(arr1) and r >= 0:
    sum = arr1[l] + arr2[r]
    tempdiff = abs(sum - k)
    print("tempdiff is ", arr1[l] , arr2[r], tempdiff, diff)
    if tempdiff < diff:
        print("Entered here")
        diff = tempdiff
        arr1_val = arr1[l]
        arr2_val = arr2[r]
        r -= 1
    else:
        l += 1

print(arr1_val, arr2_val)