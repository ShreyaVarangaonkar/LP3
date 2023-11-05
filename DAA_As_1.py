# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    n = 9
    print(fibonacci(n))

print("\nTime Complexity: O(2^n) or exponential.")
print("\nSpace Complexity: O(n) if we consider the function call stack size, otherwise O(1).")
# Fibonacci Series using Dynamic Programming
def fibonacci(n):
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(9))
print("\nTime complexity: O(n) for given n")
print("\nAuxiliary space: O(n)")
