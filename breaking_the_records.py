def breakingRecords(scores):    
    min = max = scores[0]
    min_count = max_count = 0
    for i in scores[1:]:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
    print(max_count, min_count)


n=int(input())
scores=list(map(int,input().split()))
result=breakingRecords(scores)
