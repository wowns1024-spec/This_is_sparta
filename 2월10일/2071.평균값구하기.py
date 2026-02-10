# 테스트 케이스 수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 10개의 수
    N = 10

    # 수 입력 받기
    num = map(int, input().split())

    # 평균값 출력하기
    # 더한값 저장하기
    sum = 0

    # for문을 이용하여 수 하나씩 꺼내서 sum에 더해서 넣기
    for i in num:
        sum += i

    # 평균값 구하기
    ans = sum / N

    # 소수점 첫째 자리에서 반올림한 정수를 출력해야 함
    # round 함수 사용
    print(f'#{tc} {round(ans)}')