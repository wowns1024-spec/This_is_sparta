# 최빈수 구하기

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 테스트 케이스 번호
    _ = int(input())

    # 점수 배열
    arr = list(map(int, input().split()))

    # 카운팅 정렬 과정 이용

    # 점수 배열의 최대값 구하기
    max_v = 0
    for i in range(1000): # 학생 수는 1,000명
        if max_v < arr[i]:
            max_v = arr[i]

    # 카운팅 정렬을 위한 임시 저장소 생성
    COUNTS = [0] * (max_v  + 1)

    # arr에서 튀어나오는 숫자들 COUNTS에 집어넣기
    for i in arr:
        COUNTS[i] += 1

    # 최빈값 구하기
    max_idx = 0
    for i in range(max_v+1):
        if COUNTS[max_idx] <= COUNTS[i]: # 최빈수가 여러 개인 테스트 케이스도 존재하므로 등호를 사용
            max_idx = i

    print(f'#{tc} {max_idx}')
