def rotate90(arr):
    N = len(arr)
    rotated = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            rotated[c][N-1-r] = arr[r][c]

    return rotated


def rotate180(arr):
    N = len(arr)
    rotated = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            rotated[N-1-r][N-1-c] = arr[r][c]

    return rotated

def counter_rotate90(arr):
    N = len(arr)
    rotated = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            rotated[N-1-c][r] = arr[r][c]

    return rotated


if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate90(arr))
    print(rotate180(arr))
    print(counter_rotate90(arr))