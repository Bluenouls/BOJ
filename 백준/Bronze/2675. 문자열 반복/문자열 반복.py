T = int(input())
for i in range(T):
    data = input().split()
    R=int(data[0])
    S= data[1]

    for J in S:
        print(J*R,end="")
    print()
        

