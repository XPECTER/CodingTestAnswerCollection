import sys

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    age, name = input().rstrip().split()
    lst.append((int(age), name))

lst.sort(key=lambda x: x[0])
for elem in lst:
    print(f'{elem[0]} {elem[1]}')


# 6
# 100 Yong
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung
# 19 Kong
# 35 Jung
