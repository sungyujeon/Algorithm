# 백준 14500번 G5
# 테트로미노
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

tetro = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

result = 0
def tetronomino(_li, _tetro, _i, _j, _n, _m):
    global result

    for t in _tetro:
        res = 0
        for k in t:
            ni = _i + k[0]
            nj = _j + k[1]

            if 0 <= ni < _n and 0 <= nj < _m:
                res += _li[ni][nj]
            else:
                break
        else:   
            if res > result:
                result = res


for i in range(n):
    for j in range(m):
        tetronomino(li, tetro, i, j, n, m)

print(result)


