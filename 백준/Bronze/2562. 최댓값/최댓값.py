NUM = []
for i in range(9):
    n=int(input())
    NUM.append(n)

MAX = max(NUM)
INDEX= NUM.index(MAX)+1

print(MAX)
print(INDEX)
    