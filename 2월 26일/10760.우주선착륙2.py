# 우주선착륙2

# 검토해야할 구역의 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1,T+1):

    # 구역의 크기 N, M
    N, M = map(int,input().split())

    # 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]

    #상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 좌상, 우상, 우하, 좌하
    ddi = [-1, -1, 1, 1]
    ddj = [-1, 1, 1, -1]

    # 예비 후보지 개수
    ans = 0

    # 배열 탐색
    for i in range(N):
        for j in range(M):
            # 카운트 변수
            count = 0
            for x in range(4):
                # 상하좌우 무빙 구현
                ni = i+di[x]
                nj = j+dj[x]
                # 대각선 무빙 구현
                ndi = i+ddi[x]
                ndj = j+ddj[x]

                # 인덱스 범위 체크
                if 0 <= ni < N and 0 <= nj < M:
                    # 시작점 값보다 작으면 count +1
                    # 상 하 좌 우
                    if matrix[ni][nj] < matrix[i][j]:
                        count += 1

                if 0 <= ndi < N and 0 <= ndj < M:
                    # 대각선
                    if matrix[ndi][ndj] < matrix[i][j]:
                        count += 1

                # count가 4이상이면 후보지 조건에 맞다
                if count >= 4:
                    ans += 1
                    break # for x

    print(f'#{tc} {ans}')