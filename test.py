# # import re
# # # with open("log") as FH:
# # #     data = FH.readlines()
# # #
# # # for line in data:
# # #     match = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
# # #     if match and len([x for x in match.group(0).split(".") if int(x) <= 255 ]) == 4:
# # #         print(match.group(0))
# #
# #
# # line = "172.16.251.11"
# # match = re.search("\d\d\d\.\d\d?\d?\.\d\d\d\.\d\d\d?", line)
# # print(match.group(0))
#
#
# arr = [1,2,4,9,8,7,6,5]
#
# # def merge_sort(arr):
# #     if len(arr) > 1:
# #         mid = len(arr) // 2
# #         L = arr[:mid]
# #         R = arr[mid:]
# #         merge_sort(L)
# #         merge_sort(R)
# #         i = j = k = 0
# #         while i < len(L) and j < len(R):
# #             if L[i] < R[j]:
# #                 arr[k] = L[i]
# #                 i += 1
# #             else:
# #                 arr[k] = R[j]
# #                 j += 1
# #             k += 1
# #         while i < len(L):
# #             arr[k] = L[i]
# #             k += 1
# #             i +=1
# #
# #         while i < len(R):
# #             arr[k] = R[j]
# #             k += 1
# #             j += 1
# #
# #     print(arr)
# #
# # merge_sort(arr)
#
# def partition(arr, low, high):
#     i = low - 1
#     pivot = arr[high]
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[j], arr[i] = arr[i], arr[j]
#         arr[i+1], arr[high] = arr[high], arr[i+1]
#         return (i + 1)
#
# def quick_sort(arr, low, high):
#     if low > high:
#         pi = partition(arr, low, high)
#         quick_sort(arr,low, pi - 1)
#         quick_sort(arr,pi + 1, high)
#
#     print(arr)
#
# low = 0
# high = len(arr)
#
# quick_sort(arr, low, high - 1)























#
#
# new_dict = {}
# with open("filename") as F:
# 	for line in F:
# 		Line_list = line.split()
# 		for word in Line_list:
# 			if word in new_dict.keys():
# 				new_dict[word] = new_dict[word] + 1
#             else:
#                 new_dict[word] = 1
#
#
#


import polling






