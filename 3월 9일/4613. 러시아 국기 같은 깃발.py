# 러시아 국기 같은 깃발

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # N개의 줄, M개의 문자
    N, M = map(int,input().split())

    # 색정보
    matrix = [list(input()) for _ in range(N)]

    answer = float("inf")

    # 행을 나누자
    # 3가지 흰색영역, 파란영역, 빨간영역

    # ex) N=4 => i=0,1, j=1,2
    # 흰색영역이 행 인덱스 1번까지 먹으면 파란색영역은 최소한 2번행은 먹어야함
    for i in range(N-2):
        for j in range(i+1, N-1):
            count = 0

            # 0~i 까지 흰색
            for r in range(0, i+1):
                for c in range(M):
                    if matrix[r][c] != 'W':
                        count += 1

            # i+1 ~ j 까지 파란색
            for r in range(i+1, j+1):
                for c in range(M):
                    if matrix[r][c] != 'B':
                        count += 1

            # j+1 ~ N-1 까지 빨간색
            for r in range(j+1, N):
                for c in range(M):
                    if matrix[r][c] != 'R':
                        count += 1

            answer = min(answer, count)

    print(f"#{tc} {answer}")

