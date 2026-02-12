# 농작물 수확하기

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 농장의 크기
    N = int(input())

    # 농장 내 농작물의 가치
    matrix = [list(map(int,input())) for _ in range(N)]

    # 중간 인덱스
    mid = N // 2

    # 합 저장소
    ans = 0

    start = mid
    end =mid

    for i in range(N):
        for j in range(start, end+1):
            # 처음 0행
            ans += matrix[i][j]

        # 행 인덱스가 중간인덱스보다 작을때는 시작점과 끝점 간격이 넓어진다.
        if i < mid:
            start -= 1
            end += 1

        # 그 외에는 점점 간격이 좁아진다.
        else:
            start += 1
            end -= 1


    print(f'#{tc} {ans}')



