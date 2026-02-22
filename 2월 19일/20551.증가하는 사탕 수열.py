# 증가하는 사탕 수열

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T + 1):

    # A,B,C 각각의 상자에 들어가있는 사탕 개수
    A, B, C = map(int, input().split())

    # C가 2이하로 주어지면 조건을 만족할 수 없다.
    if C <= 2:
        print(f'#{tc} -1')
        continue

    # 우선 B가 C보다 작아지려면
    # 이미 작은 상태일수도 있음 이때는 빼면 음수가 나오기 때문에
    # max함수써서 판별
    count_B = max(0, B-C+1)
    # B에서 B를 먹어치운 횟수 빼주기
    answer_B = B - count_B

    # B가 1이하이면 조건을 만족할 수 없다.
    if answer_B <= 1:
        print(f'#{tc} -1')
        continue

    # A도 마찬가지로
    count_A = max(0, A-answer_B+1)
    answer_A = A - count_A

    # A가 0이하이면 조건을 만족할 수 없다.
    if answer_A <= 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {count_A + count_B}')




