#import enum
a = "ababaabccdefghsdsdaxz"
# new_dict = {}
# for i in a:
#     try:
#         new_dict[i] += 1
#     except KeyError:
#         new_dict[i] = 1
#
# print(new_dict)

new_lis = []
index = 0

while True:
    var = 0
    for i in range(len(a) - 1):
        if a[i] == a[i+1]:
            index = i+2
            while True:
                if a[i] == a[index]:
                    index += 1
                else:
                    break
            a = a[:i] + a[index + 1:]
            var = 1
            break
    if var == 0:
        break


print(a)

###Hello This is code for nitesh1 branch121