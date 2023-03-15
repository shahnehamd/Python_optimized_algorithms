# TIME COMPLEXITY - fibo recursion - 2^n - exponential complexity

def fibo(n):
    # for 0 1 1 2 3 5 8
    # idx 0 1 2 3 4 5 6
    if n==0 or n==1:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(6))


# Memoized fibonacci - O(n)
# l is memo

l = [0,1]
def f(n):
    print(n)
    if len(l)>n:
        return l[n]
    new_fibo = f(n-1)+f(n-2)
    l.append(new_fibo)
    return new_fibo
print(f(7))


# O(n) - time complexity
# O(n) - space complexity
# no recursive stack
# optimal - since space complexity O(n)
l = [0,1]
n = 4300
for i in range(2, n+1):
    l.append(l[i-1]+l[i-2])
print(l)

# optimal - Dynamic Programming approach.
# O(n) - time complexity
# O(1) - space complexity
l = [0,1]
n = 1000
for i in range(2, n+1):
    l[0], l[1] = l[1], (l[0]+l[1])
print(l)
