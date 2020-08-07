n = 10
num_lis = [True for i in range(n+1)]
i = 2
while(i*i <= n):
    if num_lis[i] is True:
        for val in range(i*i, n+1, i):
            num_lis[val] = False
    i += 1

val_lis = [i for i in range(2, n+1) if num_lis[i] is True]
print(val_lis)
