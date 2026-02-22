# 돌 뒤집기 게임 1

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
        a, b = map(int,input().split())
        # 인덱스 변환
        start = a - 1
        end = start + b

        # 반복문을 통해 start돌과 같은 돌로 하나씩 바꿔간다.
        # end의 값이 돌의 개수보다 많으면 인덱스를 벗어나므로, 이를 방지하기 위해
        # end가 N을 넘어갈때 min함수를 통해 N을 가져온다.
        for j in range(start, min(N, end)):
            rocks[j] = rocks[start]

    print(f'#{tc}', *rocks)
