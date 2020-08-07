a = "hello my name is nitesh"
count = len([x for x in a if x == " "])
print(count)

import re
a = "nitesh nitesh nites nite"
b = re.compile(r"nites")
lis = b.findall(a)
print(lis)

#mac address can be AB:AB:12:12:12:12 or ABAB:1212:1212
# write a program to match valid mac address
mac = "12:12:12:12:12:12"
b = re.compile(r"([0-9]|[A-F])([0-9]|[A-F]):([0-9]|[A-F])([0-9]|[A-F]):([0-9]|[A-F])([0-9]|[A-F]):([0-9]|[A-F])([0-9]|[A-F])")
b = re.compile(r"(([0-9a-fA-F]):?){12}")
match = b.search(mac)
print(match.group(2))

a = "hello world world"
import re
b = re.sub("world", "!there", a,1)
print(b)
import copy
old_list = [[1],[2],[3],[4],[5]]
new_list = copy.copy(old_list)

old_list[2][0] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

class A:
    def process(self):
        print('A process()')


class B(A):
    def process(self):
        print('B process()')


class C(A, B):
    pass


obj = C()
obj.process()