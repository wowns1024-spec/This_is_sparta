# 돌 뒤집기 게임 2

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # N개의 돌, M개의 줄
    N, M = map(int, input().split())

    # 돌 초기 정보
    rocks = list(map(int, input().split()))

    for i in range(M):
        # 뒤집기 정보
        a_start, b_end = map(int,input().split())

        # 인덱스 변환
        start = a_start - 1
        end = b_end + 1

        for j in range(1, end):


            # 회문검사와 비슷
            # start에서 가까운곳 부터 비교해가자
            # 좌측, 우측 같으면 반전, 다르면 그대로 두기
            # 비교하기전에 인덱스 검사먼저하고, 만약 인덱스 벗어나면 break
            if 0 <= start - j and start + j <= N - 1:
                if rocks[start-j] == 1 and rocks[start-j] == rocks[start+j]:
                    rocks[start - j] , rocks[start + j] = 0, 0
                    continue

                if rocks[start-j] == 1 and rocks[start-j] != rocks[start+j]:
                    continue

                if rocks[start-j] == 0 and rocks[start-j] == rocks[start+j]:
                    rocks[start - j] , rocks[start + j] = 1, 1
                    continue

                if rocks[start-j] == 0 and rocks[start-j] != rocks[start+j]:
                    continue

            else:
                break # for j


    print(f'#{tc}', *rocks)