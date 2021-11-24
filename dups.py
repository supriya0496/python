def dup(inp):
    non_dup = []
    count = 0
    for ele in inp:
        if ele not in non_dup:
            non_dup.append(ele)

        else:
            count+=1
    print(count)

dup("sttrrinnngggg")
            
