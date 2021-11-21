org = list(input())
sub = list(input())
result = 0

for i in range(0, len(org)):
    if org[i] == sub[0]:
        pos = i
        count = 0
        for letter_sub in sub:
            if pos < len(org) and letter_sub == org[pos]:
                count += 1
                pos += 1
        if count == len(sub):
            result += 1
    
print(result)