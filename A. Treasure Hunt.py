# Kamrul Hasan
# 221071001
# Problem: A. Treasure Hunt

def solve():
    t = int(input())
    for _ in range(t):
        x, y, a = map(int, input().split())
        total_depth = 0
        day = 1
        while True:
            if day % 2 != 0:
                total_depth += x
                if total_depth > a:
                    print("NO")
                    break
            else:
                total_depth += y
                if total_depth > a:
                    print("YES")
                    break
            day += 1

solve()
