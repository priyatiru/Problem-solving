def countApplesAndOranges(s,t,a,b,apples,oranges):
    count_apple=0
    count_orange=0

    for i in range(len(apples)):
        sum1=apples[i]+a
        if sum1 in range(s,t+1):
            count_apple+=1
    for i in range(len(oranges)):
        sum2=oranges[i]+b
        if sum2 in range(s,t+1):
            count_orange+=1
    
    print(count_apple,count_orange,sep="\n")
    
    
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)