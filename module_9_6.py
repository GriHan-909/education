def all_variants(text):
    count = 1
    while count<=len(text):
        for i in range(len(text)):
            if (i+count) > len(text):
                continue            
            yield text[i:i + count]
        count+=1


a = all_variants("abc")
for i in a:
    print(i)