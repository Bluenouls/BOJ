import sys
input = sys.stdin.readline

n = int(input())
lis = []

for i in range(n):
    age,name = input().split()
    lis.append((age,name))

key = lambda x:int(x[0]) 
lis.sort(key = key)

for age,name in lis:
    print(age,name)
