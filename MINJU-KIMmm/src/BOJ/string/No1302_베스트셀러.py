N = int(input())
dic = dict()

for _ in range(N):
    string = input()
    if string in dic:
        dic[string]+=1
    else:
        dic[string] = 1

result = []
for key in dic:
    val = dic.get(key)
    result.append((val, key))

result.sort(key=lambda x:(-x[0], x[1]))
print(result[0][1])