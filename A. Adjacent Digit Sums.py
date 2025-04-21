#Kamrul Hasan 
#221071001

import sys

def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        d = y - x
        # ⇔ d <= 1 and (d - 1) % 9 == 0
        if d <= 1 and (d - 1) % 9 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
