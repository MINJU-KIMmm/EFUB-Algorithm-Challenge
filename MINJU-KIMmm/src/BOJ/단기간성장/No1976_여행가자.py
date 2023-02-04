N = int(input())
M = int(input())
graph = []


for i in range(N):
    inputs = list(map(int, input().split()))
    temp = []
    for j in range(N):
        if inputs[j]:
            temp.append(j)
    graph.append(temp)

plan = list(map(int, input().split()))


def find(x, parent):
    if x!=parent[x]:
        parent[x] = find(parent[x], parent)

    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N)]

for i in range(N):
    connect = graph[i]
    for c in connect:
        union(i, c, parent)

for i in range(M-1):
    now = plan[i] - 1
    next = plan[i+1] -1

    if parent[now] != parent[next]:
        print("NO")
        exit(0)


print("YES")
