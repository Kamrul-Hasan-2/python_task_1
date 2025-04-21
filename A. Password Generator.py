#Kamrul Hasan
#221071001
# Problem: A. Password Generator
def generate_password(a, b, c):
    digits = '0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    password = []
    
    while a > 0 or b > 0 or c > 0:
        if a > 0:
            password.append(digits[a % 10])
            a -= 1
        if b > 0:
            password.append(uppercase[b % 26])
            b -= 1
        if c > 0:
            password.append(lowercase[c % 26])
            c -= 1
    
    return ''.join(password)

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(generate_password(a, b, c))

solve()
