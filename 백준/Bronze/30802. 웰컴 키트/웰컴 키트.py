N = int(input())
lis = list(map(int,input().split()))
T,P= map(int,input().split())
t_bundle = 0
for i in lis:
    t_bundle += (i + T - 1) // T
print(t_bundle)


p_bundle = N//P
pen = N%P
print(p_bundle, pen)



