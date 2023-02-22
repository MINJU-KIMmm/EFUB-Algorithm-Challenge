k = int(input())
arr = list(input().split()) # 부등호 기호
nums = []
visited = [0]*10


def dfs(depth, num):
    if depth == k+1:
        nums.append(num)
        return

    for i in range(0, 10):
        if depth==0 or check(depth, num+str(i)):
            if not visited[i]:
                visited[i] = 1
                dfs(depth+1, num+(str(i)))
                visited[i] = 0


def check(i, num):
    if arr[i-1] == '<':
        if int(num[-2]) > int(num[-1]):
            return False
    else:
        if int(num[-2]) < int(num[-1]):
            return False

    return True


dfs(0, '')
print(nums[-1])
print(nums[0])
