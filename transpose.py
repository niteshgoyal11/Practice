# l = [[1,2],[3,4],[5,6]]
#
# i = 0
# new_list = []
# while i < len(l[0]):
#     temp_list = []
#     j = 0
#     while j < len(l):
#         temp_list.append(l[j][i])
#         j += 1
#     new_list.append(temp_list)
#     i += 1
#
# print(new_list)
#
#
# transpose = [[ l[j][i] for j in range(len(l)) ] for i in range(len(l(0))) ]
# print("value of ranas", transpose)

matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)

print(list(t_matrix))