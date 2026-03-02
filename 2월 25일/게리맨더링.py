# 게리맨더링
from collections import deque

# 구역의 개수 N
N = int(input())

# 각 구역의 인구
people = list(map(int,input().split()))

# 그래프 정보를 받아오기 위해 생성
graph = [[] for _ in range(N)]

# 그래프 정보 받기
for i in range(N):
    info = list(map(int,input().split()))
    # info 의 2번째 요소부터 인접 그래프 정보임
    for j in info[1:]:
        # 인접 그래프 정보를 인덱스화 시키기 위해 -1
        graph[i].append(j-1)

# 구역 나누기 함수 정의
def connected(red):

    # red가 0이면 불가능한 방법이다. 각 선거구는 적어도 하나의 구역을 포함해야 한다.
    if red == 0:
        return False

    # 시작 정점 찾기
    start = -1
    for i in range(N):
        # ex) red == 7 일때 000111,  i = 0이고 (1<<i)는 000001. and 연산자 사용하면 True.
        if red & (1 << i):
            start = i
            break # for i

    # 시작 정점 찾았으면 인접한 정점 찾자
    q = deque([start])
    # 방문했는지 알기 위해서 변수 설정
    visited = 0
    # 시작 정점은 방문처리
    visited |= (1 << start)

    # q에 무언가 남아있는 동안 계속해서 실행
    while q:
        x = q.popleft()

        for nx in graph[x]: # graph[0]이 [1,3] 일 경우 인덱스화 된 정점들이니까 2번 4번 정점과 맞닿아 있다는 것
            # nx가 현재 선거구(red)에 속해 있고,
            # 아직 방문하지 않은 구역이라면
            if (red & (1<<nx)) and not (visited & (1<<nx)):
                # 방문처리
                visited |= (1 << nx) # nx가 1일때 000010 2번째에 불 켜짐.
                # q에 넣기
                q.append(nx)

    # BFS로 방문한 구역들이
    # 우리가 검사하려던 red와 정확히 같으면
    # 연결되었다는것!
    return red == visited

# 각 선거구역의 인구합 구하는 함수
def sum_people(red):
    s = 0
    for i in range(N):
        if red & (1 << i):
            s += people[i]

    return s

# 마지막 단계
# 두 선거구가 모두 연결되어 있는지 체크하고
# 각 선거구역의 합 구해서 차이가 최소가 될 때를 찾아야 함

ALL = (1 << N) - 1
ans = 10 ** 18

# 대칭 제거 : 0과 ALL은 제외, 절반만 보면 된다.
for red in range(1,1 << (N-1)):
    blue = ALL ^ red # 불이 전부 켜져있는 ALL에 red와 XOR 연산 때리면 반대 부분집합 구할 수 있다.

    # 두 선거구가 모두 연결되어 있어야만 유효한 분할
    if connected(red) and connected(blue):
        diff = abs(sum_people(red) - sum_people(blue))

        if diff < ans:
            ans = diff

# 만약 유효한 분할이 한 번이라도 있었다면 -> ans 출력
# 한 번도 없었다면 -1 출력
print(ans if ans != 10**18 else -1)


