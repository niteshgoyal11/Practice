str_full = "1212121678767812167678"
substr = "121"
count = 0
for i in range(len(str_full)-len(substr) + 1):
    new_substr = str_full[i:i + len(substr)]
    print(new_substr)
    if new_substr == substr:
        count += 1

print(count)