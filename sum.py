def test_string(string_1):
    num_lis = []
    operand_lis = []
    i = 0
    while i < len(string_1):
        new_lis = ""
        if string_1[i].isdigit():
            new_lis += string_1[i]
            while i+1 < len(string_1):
                if string_1[i+1].isdigit():
                    new_lis += string_1[i+1]
                else:
                    break
                i += 1
            num_lis.append(new_lis)     
        else:
            operand_lis.append(string_1[i])
        i += 1
    sum = int(num_lis[0])
    for i in range(len(operand_lis)):
        if operand_lis[i] == "+":
            sum = sum + int(num_lis[i + 1])
        elif operand_lis[i] == "-":
            sum = sum - int(num_lis[i + 1])
    #print(num_lis, operand_lis)
    print(sum)    