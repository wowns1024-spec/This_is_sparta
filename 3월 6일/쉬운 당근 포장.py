# 쉬운 당근 포장

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 당근의 개수
    N = int(input())

    # 수확한 N개의 당근 크기 Ci
    Ci = list(map(int,input().split()))

    # 당근 크기가 오름차순으로 나오지 않을때를 고려
    Ci.sort()

    answer = 10 ** 19

    # Ci가 1,2,3 이라고 가정했을때
    # 처음 s사이즈 박스에 들어갈 당근은 1이다.
    # 따라서 범위설정을 N-2 => 3-2=1 => i=0
    for i in range(N-2):
        # 만약 다음에도 같은사이즈가 나온다면 같은 상자에 넣어야 하므로 다음 범위로 넘어가기
        if Ci[i] == Ci[i+1]:
            continue

        # Ci가 1,2,3 이라고 가정했을때
        # m사이즈 박스에 들어갈 당근은 2이다.
        # 따라서 범위설정을 i의 다음 상자부터 N-1로 설정
        # i가 0일때 j의 range(1,2)
        for j in range(i+1, N-1):
            if Ci[j] == Ci[j+1]:
                continue

            # 위에서 s사이즈,m사이즈에 들어갈 당근을 구했으면
            # 자동으로 l사이즈에 들어갈 당근들은 N-j-1로 구할 수 있다.
            s = i + 1
            m = j - i
            l = N - j - 1

            # 각 상자에는 1개이상 들어가야 조건을 만족할 수 있음
            if s > 0 and m > 0 and l > 0:

                # s.m,l 상자에서 제일 많이 들어가있는 개수 - 제일 적게 들어가있는 개수
                # 최소가 되도록
                answer = min(answer, max(s,m,l) - min(s,m,l))


    # 위에서 answer가 바뀌지 않고
    # 맨 처음에 말도안되게 높은 숫자로 설정해놓은 answer가 그대로 튀어나온다면
    # 조건을 만족하는 포장방법이 없다는것이므로 -1을 반환
    if answer == 10 ** 19:
        answer = -1

    print(f'#{tc} {answer}')