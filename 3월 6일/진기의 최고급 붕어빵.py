# 진기의 최고급 붕어빵

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 사람 수 N, 시간 초 M, 붕어빵 개수 K
    N, M, K = map(int,input().split())

    # 각 사람이 언제 도착하는지를 초 단위로 나타냄
    arrive = list(map(int,input().split()))

    arrive.sort()

    # 모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 "Possible"
    # 아니라면 "Impossible"

    # 붕어빵이 완성되면 어떤 시간 지연도 없이 붕어빵 만들기를 시작할 수 있다.
    bread = 0
    sec = 0
    answer = "Possible"
    visited = 0

    # 붕어빵 만들기도전에 사람 와버리면 조건 만족할 수 없다.
    if arrive[0] < M:
        answer = "Impossible"
    else:
        while visited != (1 << N) - 1:
            sec += 1

            # 빵 만들기
            if sec % M == 0:

                bread += K

            for i in range(N):
                if sec == arrive[i] and not (visited & (1<<i)):
                    if bread > 0:
                        bread -= 1
                        visited |= (1 << i)

                    else:
                        answer ="Impossible"
                        break
            if answer == "Impossible":
                break

    print(f'#{tc} {answer}')