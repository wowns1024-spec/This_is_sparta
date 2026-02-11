# 새로운 불면증 치료법

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 각 테스트 케이스의 N의 배수
    N = int(input()) #(1 <= N <= 10^6)

    COUNTS = [0] * 10

    # 0부터 9까지 False 로 초기화
    for i in range(10):
        COUNTS[i] = False

    num = 0

    while True:

        num += 1

        good = N * num

        good_str = str(good)

        if "0" in good_str:
            COUNTS[0] = True

        if "1" in good_str:
            COUNTS[1] = True

        if "2" in good_str:
            COUNTS[2] = True

        if "3" in good_str:
            COUNTS[3] = True

        if "4" in good_str:
            COUNTS[4] = True

        if "5" in good_str:
            COUNTS[5] = True

        if "6" in good_str:
            COUNTS[6] = True

        if "7" in good_str:
            COUNTS[7] = True

        if "8" in good_str:
            COUNTS[8] = True

        if "9" in good_str:
            COUNTS[9] = True

        # 전부 True로 스위치가 켜졌다면 break
        if COUNTS[0] and COUNTS[1] and COUNTS[2] and COUNTS[3] and COUNTS[4] and COUNTS[5] and COUNTS[6] and COUNTS[7] and COUNTS[8] and COUNTS[9]:
            answer = good
            break

    print(f'#{tc} {good}')
