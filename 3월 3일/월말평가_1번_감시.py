# 월말평가2 - 문제1 : 감시

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 격자의 크기 N
    N = int(input())

    # 2차원 배열
    matrix = [list(map(int,input().split())) for _ in range(N)]

    # 델타
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 0 : 통로
    # 1 : 벽
    # 2 : 술래

    for i in range(N):
        for j in range(N):
        # 2차원 배열 탐색해서 술래찾기
            if matrix[i][j] == 2:
                # 시뮬레이션 좌표
                si, sj = i, j

                # 델타 탐색
                for x in range(4):
                    # 술래의 감시 범위
                    for z in range(1, N):
                        ni = si + di[x]*z
                        nj = sj + dj[x]*z

                        # 인덱스 범위 검사, 통로인지 검사
                        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0:
                            # 검사 통과 되면 술래의 영향이 미치는 곳이기 때문에 값을 3으로 변경!
                            matrix[ni][nj] = 3

                        else:
                            # 벽을 만났을때 break 하지 않으면 벽을 넘어서까지 영향을 미쳐버림.
                            break # for z
    print(matrix)
    # 완전 탐색을 통해 안전한 곳을 카운트해서 찾자
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                count += 1

    print(f'#{tc} {count}')



