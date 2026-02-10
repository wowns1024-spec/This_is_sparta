# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 반복문
for tc in range(1, T+1):

    # 학생수 N, 학점을 알고싶은 학생의 번호 K
    N, K = map(int, input().split())

    # 중간, 기말, 과제 점수
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 성적
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    # 함수 정의해보기
    def score(scores):
        mid, final, assignment = scores

        total = (mid * 0.35) + (final * 0.45) + (assignment * 0.2)

        return total

    # 일괄 적용
    result = list(map(score, arr))

    # k번째 학생의 총점
    ans = result[K-1]

    # reverse=True 한 이유는 학점은 점수 높은 사람이 앞에 오기 때문
    sorted_scores = sorted(result, reverse=True)

    # index 0 -> 1등 / index 1 -> 2등
    rank = sorted_scores.index(ans)
    # 이게 핵심
    # 학생수가 100명이면 a+부터 D0 까지 10명씩 주기 위함
    group_size = N // 10
    grade = grades[rank // group_size]

    print(f'#{tc} {grade}')




