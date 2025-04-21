# Problem: A. To Zero
#Kamrul Hasan
#221071001
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print(n // 2)
    else:
        print(1 + (n - 1) // 2)
        
