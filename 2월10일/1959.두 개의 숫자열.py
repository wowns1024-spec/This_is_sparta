# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # N 개의 숫자로 구성된 숫자열 Ai, M 개의 숫자로 구성된 숫자열 Bj
    N, M = map(int,input().split())

    # Ai 숫자열
    A = list(map(int, input().split()))
    # Bj 숫자열
    B = list(map(int, input().split()))

    # 최대값 변수 초기화
    max_v = 0

    # N=M 일때는 반복문 이용해서 인덱스에 맞게 계산
    # N<M 이거나 N>M 일때
    # 길이가 작은쪽 숫자열은 항상 곱셈의 대상이 된다
    # 따라서 길이가 큰쪽의 숫자열에 해당하는 요소들의 인덱스를 움직여줘야 한다.
    # N과 M의 차이만큼.
    # range()에 들어가니까 +1 해줘야 한다.



    # N = M 일때
    if N == M:
        for i in range(N):
            max_v += (A[i] * B[i])

    # N > M 일때
    elif N > M:
        C = N-M+1
        for i in range(C):
            ans = 0
            for j in range(M):
                ans += (A[i+j] * B[j])
            if max_v < ans: # 최대값 찾기
                max_v = ans

    # N < M 일때
    elif N < M:
        C = M-N+1
        for i in range(C):
            ans = 0
            for j in range(N):
                ans += (A[j] * B[i+j])
            if max_v < ans: # 최대값 찾기
                max_v = ans

    print(f'#{tc} {max_v}')