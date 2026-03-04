# 1873. 상호의 배틀필드

# 테스트 케이스
T = int(input())

# 테스트 케이스 반복문
for tc in range(1,T+1):

    # 게임 맵의 높이 H, 너비 W
    H, W = map(int,input().split())

    game_map = [[0]*W for _ in range(H)]

    for i in range(H):
        game_map[i] = list(input())

    # 길이
    N = int(input())

    # 길이가 N인 문자열
    arr = input()

    # 완전탐색으로 전차 위치를 파악
    for i in range(H):
        for j in range(W):
            if game_map[i][j] in "^v<>":
                # 전차 위치
                si, sj = i, j
                break


    # 게임 시작
    for i in arr:

        # 탱크 움직임 처리
        # UP : 전차 방향 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 그 칸으로 이동
        if i == "U":
            game_map[si][sj] = "^"

            # 인덱스 검사, 해당 칸이 평지인지 검사
            if 0 <= si-1 < H and game_map[si-1][sj] == ".":
                # 전차이동
                game_map[si-1][sj] = "^"
                # 원래위치 평지화
                game_map[si][sj] = "."

                # 탱크 위치 최신화
                si = si - 1

            # 만족하지 못하면 패스
            else:
                continue



        # Down : 전차 방향 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동
        elif i == "D":
            game_map[si][sj] = "v"
            if 0 <= si+1 < H and game_map[si+1][sj] == ".":
                # 전차이동
                game_map[si+1][sj] = "v"
                # 원래위치 평지화
                game_map[si][sj] = "."

                # 탱크 위치 최신화
                si = si + 1

            else:
                continue



        # Left : 전차 방향 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동
        elif i == "L":
            game_map[si][sj] = "<"
            if 0 <= sj - 1 < W and game_map[si][sj - 1] == ".":
                # 전차이동
                game_map[si][sj-1] = "<"
                # 원래위치 평지화
                game_map[si][sj] = "."

                # 탱크 위치 최신화
                sj = sj - 1

            else:
                continue

        # Right : 전차 방향 오른쪽으로 바꾸고, 한 칸이 오른쪽의 칸이 평지라면 그 칸으로 이동
        elif i == "R":
            game_map[si][sj] = ">"
            if 0 <= sj + 1 < W and game_map[si][sj + 1] == ".":
                # 전차이동
                game_map[si][sj + 1] = ">"
                # 원래위치 평지화
                game_map[si][sj] = "."

                # 탱크 위치 최신화
                sj = sj + 1

            else:
                continue


        # Shoot : 전차가 바라보고 있는 방향으로 포탄 발사
        # 포탄을 쏴도 전차는 움직이지 않아야 한다.
        # 포탄 좌표는 따로 관리

        # 포탄 발사
        # 벽 -> 포탄 소멸
        # if 벽이 벽돌? -> 파괴 -> 평지화
        # if 벽이 강철? -> 아무일x
        # 맵 밖으로 포탄? -> 아무일x

        elif i == "S":

            # 포탄 좌표
            bi , bj = si, sj



            # 왼쪽으로 발사
            if game_map[si][sj] == "<":

                while 0 <= bj-1 < W:

                    # 통과하면 지형지물 체크
                    # 평지일때, 물일때
                    if game_map[bi][bj-1] in ".-":
                        # 포탄 좌표 최신화
                        bj = bj - 1

                    # 벽돌로 만들어진 벽일때
                    elif game_map[bi][bj-1] == "*":
                        # 포탄 소멸, 칸 평지화
                        game_map[bi][bj-1] = "."
                        break

                    # 강철로 만들어진 벽일때
                    elif game_map[bi][bj-1] == "#":
                        # 포탄 소멸
                        break

            # 오른쪽으로 발사
            elif game_map[si][sj] == ">":

                while 0 <= bj+1 < W:
                    # 통과하면 지형지물 체크
                    # 평지일때, 물일때
                    if game_map[bi][bj+1] in ".-":
                        # 포탄 좌표 최신화
                        bj = bj + 1

                    # 벽돌로 만들어진 벽일때
                    elif game_map[bi][bj+1] == "*":
                        # 포탄 소멸, 칸 평지화
                        game_map[bi][bj+1] = "."
                        break

                    # 강철로 만들어진 벽일때
                    elif game_map[bi][bj+1] == "#":
                        # 포탄 소멸
                        break

            # 위로 발사
            elif game_map[si][sj] == "^":

                while 0 <= bi-1 < W:
                    # 통과하면 지형지물 체크
                    # 평지일때, 물일때
                    if game_map[bi-1][bj] in ".-":
                        # 포탄 좌표 최신화
                        bi = bi -1

                    # 벽돌로 만들어진 벽일때
                    elif game_map[bi-1][bj] == "*":
                        # 포탄 소멸, 칸 평지화
                        game_map[bi-1][bj] = "."
                        break

                    # 강철로 만들어진 벽일때
                    elif game_map[bi-1][bj] == "#":
                        # 포탄 소멸
                        break

            # 아래로 발사
            elif game_map[si][sj] == "v":

                while 0 <= bi+1 < W:
                    # 통과하면 지형지물 체크
                    # 평지일때, 물일때
                    if game_map[bi+1][bj] in ".-":
                        # 포탄 좌표 최신화
                        bi = bi + 1

                    # 벽돌로 만들어진 벽일때
                    elif game_map[bi+1][bj] == "*":
                        # 포탄 소멸, 칸 평지화
                        game_map[bi+1][bj] = "."
                        break

                    # 강철로 만들어진 벽일때
                    elif game_map[bi+1][bj] == "#":
                        # 포탄 소멸
                        break

    # 출력
    print(f"#{tc}", end=" ")
    for i in range(H):
        print(''.join(game_map[i]))

# 살려주세요 강사님.
# 런타임에러가 떠요