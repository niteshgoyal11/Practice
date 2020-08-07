

def fibonicci(n):
    new_list = [1,1,2,3]
    for i in range(1,n+1):
        num = new_list[i-1] + new_list[i]
        new_list.append(num)


fibonicci(15)