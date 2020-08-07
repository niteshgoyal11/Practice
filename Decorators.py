def sample_decorator(func):
    def _wrapper(*args, **kwargs):
        print("Before callinnctiong this function")
        print("Got argumanets as", args)
        print("Got argumanets as", kwargs)
        func(*args)
        print("After calling function")
    return _wrapper

@sample_decorator
def sample_function(a,b,c):
    print(a+b+c)
    print("I am calling this functon with ")

sample_function(1,2,3,val=4)

#
# def test_string(string_1):
#     num_lis = []
#     operand_lis = None
#     i = 0
#     iteration = 1
#     new_lis = ""
#     first_elem = None
#     second_elem = None
#     while i < len(string_1):
#         if string_1[i].isdigit():
#             new_lis += string_1[i]
#             while i+1 < len(string_1):
#                 if string_1[i+1].isdigit():
#                     new_lis += string_1[i+1]
#                 else:
#                     break
#                 i += 1
#         else:
#             operand_lis = string_1[i]
#
#         if first_elem is None:
#             first_elem = int(new_lis)
#             new_lis = ""
#         elif second_elem is None and first_elem is not None:
#             if new_lis == "":
#                 pass
#             else:
#                 second_elem = int(new_lis)
#                 if operand_lis == "+":
#                     first_elem = first_elem + second_elem
#                 else:
#                     first_elem = first_elem - second_elem
#                 second_elem = None
#                 new_lis = ""
#         i += 1
#     print("sum is ", first_elem)
# test_string("2+20-5")
# test_string("2+20-5")
# test_string("200+20-5-5-6-7-4")