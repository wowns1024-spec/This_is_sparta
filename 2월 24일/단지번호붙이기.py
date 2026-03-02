# 단지번호붙이기

# 지도의 크기
N = int(input())

# 2차원 배열
matrix = [list(map(int,input())) for _ in range(N)]

# 재귀 없이 풀어보기
# 델타
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

sizes = []

# 2차원 배열 탐색
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            # 방문처리
            matrix[i][j] = 0

            # 재귀 없이 풀려면 스택이 필요!
            stack = [(i,j)]

            # 카운트 변수 생성
            count = 0

            # DFS 탐색
            # stack에 무언가 남아있는 동안 계속해서 탐색
            while stack:
                # 시뮬레이션 좌표
                si, sj = stack.pop()
                # 탐색횟수
                count += 1

                for x in range(4):
                    ni = si + di[x]
                    nj = sj + dj[x]

                    # 인덱스 범위 검사, 방문 검사
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1:
                        # 방문처리
                        matrix[ni][nj] = 0
                        # 스택에 푸쉬
                        stack.append((ni,nj))

            # count 횟수 저장
            sizes.append(count)

print(len(sizes))
sizes.sort()
for i in sizes:
    print(i)