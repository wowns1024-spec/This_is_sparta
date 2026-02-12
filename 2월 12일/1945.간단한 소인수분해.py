# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1,T+1):


    # 숫자 N
    N = int(input()) # (2 <= N <= 10,000,000)

    # 정답
    ans =[]

    for i in [2,3,5,7,11]:
        count = 0
        # i로 나누었을 때 나머지가 0이 될 때까지 실행
        while N % i == 0:
            # N을 i로 나누었을 때 몫을 다시 N에 저장
            N //= i
            # 연산이 될 때마다 count +1
            count += 1
            # N % i 가 0이 아닐때 count에 쌓여있는 값을 ans 리스트에 넣기
        ans.append(count)


    print(f'#{tc}', *ans)