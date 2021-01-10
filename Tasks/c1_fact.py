def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    else:
        if n == 1:
            return n
        return factorial_recursive(n-1)*n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    i = 1
    fact = i
    while i <= n:
        fact *= i
        i += 1
    return fact


# import math
# if __name__ == '__main__':
#     print(math.factorial(12),factorial_iterative(12))
#     print(math.factorial(12), factorial_recursive(12))
