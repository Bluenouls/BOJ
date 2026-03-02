import sys
def starline(n):
    if n ==1:
        return["*"]
    stars=starline(n//3)
    L=[]

    for i in stars:
        L.append(i*3)


    for i in stars:
        L.append(i + " " * (n // 3) + i)
    
    for i in stars:
        L.append(i * 3)
    
    return L

line = sys.stdin.readline().strip()
if line:
    N = int(line)
    print('\n'.join(starline(N)))