def kangaroo(x1,v1,x2,v2):
    if (x2-x1) * (v2-v1) <0 and (x2 - x1) % (v2 - v1) == 0 :
        print("YES")
    else:
        print("NO")    


x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
