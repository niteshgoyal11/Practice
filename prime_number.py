
n = 9999999967
def prime(num):
    if num <= 1:
        return False
    i = 2
    while(i*i <= num):
        print(i)
        if num % i == 0:
            return False
        i += 1
    return True

print(prime(n))