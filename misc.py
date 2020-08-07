# lis = ["1", "2", "3", "4"]
#
# new_dict = {lis[i]: lis[i + 1] for i in range(0,len(lis), 2)}
# print(new_dict)
# print(type(new_dict))
#
# a = ["John", "Charles", "Mike", "Mike"]
# b = ["Jenny", "Christy", "Monica"]
#
#
#
# x = zip(a, a)
# print(dict(x))
#
# arr = [1,2,3,4,5,6,7,8]
#
# # for i in range(len(arr)):
# #     temp = i + 2
# #     if temp >= len(arr):
# #         break
# #     arr[i],arr[temp] = arr[temp], arr[i]
# #
# # print(arr)
#
# temp = [1,2]
# arr = arr[2:]
# arr = arr + temp
# print(arr)

####Finding unique divisor
#
# n = 1000
# red_lis = [i for i in range(1, n+1) if n %i == 0]
# print (red_lis)
#
# lis = []
# temp = n + 1
# for i in range(1,temp):
#     if n % i == 0:
#         if i in lis:
#             continue
#         lis.append(i)
#         lis.append(n // i)
#         temp = n // i
#
# print(lis)


### Leader in array
#
# arr = [16, 17, 4, 3, 5, 2]
# leader_lis = []
# for i in range(len(arr) - 1):
#     leader_flag = 1
#     for j in range(i+1,len(arr)):
#         if arr[i] < arr[j]:
#             leader_flag = 0
#             break
#     if leader_flag == 1:
#         leader_lis.append(arr[i])
#
# leader_lis.append(arr[-1])
#
# print(leader_lis)

# import time
# arr = [16, 17, 4, 3, 5, 2]
#
# greatest_elem = None
# def max_index(arr):
#     #print(arr)
#     greatest_elem = arr[0]
#     greatest_index = 0
#     for i in range(1,len(arr)):
#         if greatest_elem < arr[i]:
#             greatest_elem = arr[i]
#             greatest_index = i
#     return greatest_index
#
# leader_lis = []
# index = -1
# fix_value = 0
# iter = 0
# while True:
#     if fix_value >= len(arr):
#         break
#     print(arr[index+1:])
#     index = max_index(arr[index+1:])
#     print(index)
#     fix_value = fix_value + index + iter
#     print(fix_value)
#     leader_lis.append(arr[fix_value])
#     print(leader_lis)
#     iter += 1
#
# print(leader_lis)


##################################

# #Find third largest number
#
# arr = [1,2,3,4,5,6,7,8,9]
# first = None
# second = None
# third = None
#
# for i in range(len(arr)):
#     if first is None:
#         first = arr[i]
#     elif arr[i] > first and second is None:
#         second = first
#         first = arr[i]
#     elif arr[i] > second and third is None:
#         third = second
#         second = arr[i]
#     elif arr[i] > first:
#         third = second
#         second = first
#         first = arr[i]
#     elif arr[i] > second:
#         third = second
#         second = arr[i]
#     elif arr[i] > third:
#         third = arr[i]
#
# print(first,second,third)

##########sorting string###############

# a = "ddccbbaa"
# charcount = [0 for i in range(1,27)]
# for i in a:
#     charcount[ord(i) - ord("a")] += 1
#
# print(charcount)
#
# for i in range(len(charcount)):
#     if charcount[i] == 0:
#         continue
#     val = (chr(ord("a") + i)) * charcount[i]
#     print(val, end = "")

############Factorial #################

# n = 4
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(4))

def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point

# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
         break
    print(num)