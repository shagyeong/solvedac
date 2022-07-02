import sys
input = sys.stdin.readline

def pentapenta(n):
    return ((3 * n + 8) * (n - 1)) // 2 + 5

n = int(input())
print(pentapenta(n) % 45678)
