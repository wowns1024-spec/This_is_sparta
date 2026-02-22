# 원재의 메모리 복구하기

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 메모리의 원래 값
    memory = list(map(int, input()))

    # 고친횟수
    count = 0

    # 인덱스 0번부터 차근차근
    # 1만나면 count + 1
    # 1만나고 0만나면 count + 1
    # 0만났다가 1만나면 count + 1

    # 처음상태
    switch = False

    for i in memory:
        if switch == False and i == 1:
            switch = True
            count += 1
            continue

        if switch == True and i == 0:
            switch = False
            count += 1
            continue

    print(f'#{tc} {count}')


