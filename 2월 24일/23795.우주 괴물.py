# 우주 괴물

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 가로,세로 N칸
    N = int(input())

    # 2차원 배열
    matrix = [list(map(int,input().split())) for _ in range(N)]

    # 괴물의 위치 파악
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                monster_i, monster_j = i, j

    # 시뮬레이션 좌표
    mi, mj = monster_i, monster_j
    i = 1

    # 딱히 필요없는 변수
    check = 0

    # 구해야 할 답
    # 안전한 칸
    count = 0

    # 상
    while True:

        # 고려해야 할 사항
        # 다음칸이 인덱스 범위 내?
        # 다음칸이 벽이 아닌가?
        # 범위 내이고 벽이 아니라면 값을 3으로 만들자
        if check == 0 and 0 <= mi-i < N  and matrix[mi-i][mj] != 1:
            matrix[mi-i][mj] = 3
            i += 1

        else:
            check = 1
            mi = monster_i
            i = 1
            break

    # 하
    while True:

        if check == 1 and 0 <= mi+i < N  and matrix[mi+i][mj] != 1:
            matrix[mi+i][mj] = 3
            i += 1

        else:
            check = 2
            mi = monster_i
            i = 1
            break

    # 좌
    while True:

        if check == 2 and 0 <= mj-i < N  and matrix[mi][mj-i] != 1:
            matrix[mi][mj-i] = 3
            i += 1

        else:
            check = 3
            mj = monster_j
            i = 1
            break

    # 우
    while True:

        if check == 3 and 0 <= mj+i < N  and matrix[mi][mj+i] != 1:
            matrix[mi][mj+i] = 3
            i += 1

        else:
            check = 4
            mj = monster_j
            i = 1
            break

    # 안전한 칸 구하기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                count += 1

    print(f'#{tc} {count}')