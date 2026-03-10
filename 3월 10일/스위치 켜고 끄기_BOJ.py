# 스위치 켜고 끄기

# 스위치 개수
N = int(input())

# 스위치의 상태
switch = list(map(int,input().split()))

# 학생 수
students = int(input())

# 학생의 성별(1:남자, 2:여자), 학생이 받은 수
students_info = [list(map(int,input().split())) for _ in range(students)]

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈
# 스위치 번호는 1번부터 시작
# 여학생은 받은 수의 스위치 포함 양쪽으로 퍼져나가면서 대칭인지 확인하고
# 대칭이 맞다면 상태를 바꾼다.

def on_off(info,num):

    # info = 1 남자인경우
    if info == 1:
        k = num

        # num이 N보다 작거나 같을때동안 실행
        while k <= N:

            # 스위치 상태 바꾸기
            if switch[k-1] == 1:
                switch[k-1] = 0


            else:
                switch[k-1] = 1

            k += num

    # info = 2 여자인경우
    elif info == 2:

        # 부여받은 번호에 해당하는 스위치 상태 바꾸기
        if switch[num-1] == 1:
            switch[num-1] = 0

        else:
            switch[num-1] = 1

        # 양쪽 대칭 검사후 상태 바꾸기
        for i in range(1, N):
            # 인덱스 검사
            if 0 <= num-1-i and num-1+i < N:
                # 대칭 검사, 1일때
                if switch[num-1-i] == 1 and switch[num-1-i] == switch[num-1+i]:
                    switch[num-1-i], switch[num-1+i] = 0, 0
                # 대칭 검사, 0일때
                elif switch[num-1-i] == 0 and switch[num-1-i] == switch[num-1+i]:
                    switch[num-1-i], switch[num-1+i] = 1, 1

                else:
                    break # for i

            else:
                break

    return switch


for i in range(students):
    on_off(students_info[i][0],students_info[i][1])

for i in range(0, N, 20):
    print(*switch[i:i+20])