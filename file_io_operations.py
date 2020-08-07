from time import sleep
with open("test_2.py") as F:
    #count = sum([1 for line in F for character in line if character.isupper()])
    data = F.readlines()
print(data)