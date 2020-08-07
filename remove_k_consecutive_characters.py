import time
a = "aaabbccddwrtyhgfffddsqaa"
k = 2
i = 0
while i < len(a):
    first_elem = a[i]
    count = 1
    temp = i
    while True:
        if i == len(a) - 1:
            i += 1
            break
        if a[i + 1] == first_elem:
            count += 1
            i += 1
        else:
            i += 1
            break
    if count >= k:
        a = a[0:temp] + a[i:]
        i = 0
        print(a)
        #time.sleep(1)

print(a)
