# 오목 판정

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 길이 N
    N = int(input())

    GoMoku = [input().strip() for _ in range(N)]
    print(GoMoku)

    # 돌이 다섯 개 이상 연속한 부분이 없다고 가정
    answer = False

    # 회문검사

    # 행 먼저 검사
    for i in range(N):
        for j in range(N-4):
            # 가로는 한 줄이 문자열이기 때문에 슬라이싱 가능
            if GoMoku[i][j:j+5] == "ooooo":
                answer = True
                break
        if answer:
            break

    # 열 검사
    if not answer:
        for i in range(N-4):
            for j in range(N):
                if all(GoMoku[i+k][j] == "o" for k in range(5)):
                    answer = True
                    break
            if answer:
                break

    # 우하향 대각선
    if not answer:
        for i in range(N-4):
            for j in range(N-4):
                if all(GoMoku[i+k][j+k] == "o" for k in range(5)):
                    answer = True
                    break
            if answer:
                break

    # 우상향 대각선
    if not answer:
        for i in range(N-4):
            for j in range(4, N):
                if all(GoMoku[i+k][j-k] == "o" for k in range(5)):
                    answer = True
                    break
            if answer:
                break

    if answer:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')




