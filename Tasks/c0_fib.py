def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    fib = [0, 1]
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 1:
        raise ValueError
    fib = [0, 1]
    if 1 <= n <= 2:
        return fib[n-1]
    i = 3
    prev_1 = fib[-1]
    prev_2 = fib[-2]
    while i != n+2:
        prev_1, prev_2 = prev_1+prev_2, prev_1
        i += 1
    return prev_1


if __name__ == '__main__':
    n = 9
    print(fib_iterative(n))
    print(fib_recursive(n))
