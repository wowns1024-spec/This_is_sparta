# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 10개의 수
    N = 10

    # 수 입력받기
    num = map(int, input().split())

    # 더한값을 저장하는 곳
    sum = 0

    # 홀수만 더해서 값을 출력하기
    for i in num:
        # 홀수는 2로 나누었을때 나머지가 1이 나온다.
        if i % 2 == 1:
            # 만약 홀수라면 sum변수에 더해서 넣자
            sum += i

    print(f'#{tc} {sum}')