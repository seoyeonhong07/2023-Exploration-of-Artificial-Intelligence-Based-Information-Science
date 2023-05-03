import my_util


#@mt_util.time_checker
def factorial_repetition(n):
    """
    factorial function with repetition
    :param n: > 0
    :return: n!
    """
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result


#@mt_util.time_checker
def factorial_recursion(n):
    """
    factorial function with repetition
    :param n: > 0
    :return: n!
    """
    if n == 1:
        return 1
    else:
        return n * factorial_repetition(n-1)



memo = [None for _ in range(100)]
"""
"""
#@mt_util.time_checker
def fibonacci_recursion(n):
    """
    fibonacci number function
    :param n: integer value
    :return: fibonacci number
    """
    if n <= 1:
        return n
    if memo[n] is not None:
        return memo[n]
    else:
        memo[n] = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
        return memo[n]


if __name__ == "__main__":
    number = int(input("정수 입력 : "))
    print(factorial_recursion(number))
    print(factorial_repetition(number))
    print(fibonacci_recursion(number))


