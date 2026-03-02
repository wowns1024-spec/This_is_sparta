# 단지번호붙이기 재귀버전

# 지도의 크기
N = int(input())

# 2차원 배열
matrix = [list(map(int,input())) for _ in range(N)]

# 델타
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# DFS 함수 정의
def DFS(i, j):
    matrix[i][j] = 0
    count = 1

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]

        # 인덱스 범위 검사! 방문 했는지 검사!
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1:
            count += DFS(ni,nj)

    return count

sizes = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            sizes.append(DFS(i,j))

print(len(sizes))
sizes.sort()
for i in sizes:
    print(i)
