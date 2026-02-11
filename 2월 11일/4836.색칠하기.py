# 색칠하기

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 첫 줄에 칠할 영역의 개수
    N = int(input())

    # 왼쪽 위 모서리 인덱스 r1,c1 / 오른쪽 아래 모서리 r2,c2 / 색상 정보 1(빨강) 2(파랑)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 10X10 격자 만들기
    matrix = [[0]*10 for _ in range(10)]



    for c in range(N):
        # 행
        r1 = arr[c][0]
        r2 = arr[c][2]
        # 열
        c1 = arr[c][1]
        c2 = arr[c][3]
        color = arr[c][4]  # 빨강 = 1 / 파랑 = 2
        # 범위만큼 순회하면서 값 부여하기
        for i in range(r1, r2+1): # 행 침투
            for j in range(c1, c2+1): # 열 침투

                matrix[i][j] += color # 값 부여

    # 전체 배열에서 3 개수 세기
    answer = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                answer += 1


    print(f'#{tc} {answer}')