import sys

while True:
    L = sys.stdin.readline().split()
    a, b = map(int,L)
    if a == 0 and b==0:
        break

    if a > b:
        print("Yes")
    else:
        print("No")