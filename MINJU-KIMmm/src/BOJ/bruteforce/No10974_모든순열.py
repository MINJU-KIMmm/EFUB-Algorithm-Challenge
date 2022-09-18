from itertools import permutations

#순열

n = int(input())
arr = []
for i in range(1, n+1):
    arr.append(i)


for i in permutations(arr,n):
    print(*i)

#######################33


#dfs버전


# visited = []
#
# def dfs():
#     if len(visited)==n:
#         print(*visited)
#         return
#
#     for i in range(1, n+1):
#         if i not in visited:
#             visited.append(i)
#             dfs()
#             visited.pop()
#
# dfs()