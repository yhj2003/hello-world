import sys
sys.stdin= open('text')

n,m,k = map(int,input().split())

def median(n,m,k):


    if (n>=m >= k) | (n<= m <= k):
        return m
    elif (m >= n >= k) | (m <= n <= k):
        return n
    elif (n >= k >= m) | (n <= k <= m):
        return k

print(median(n,m,k))