from sympy import isprime


def prime_aware_truncation(p):
    """
    The Prime-Aware Right-Truncation Operator R
    Series: Mathematical Foundations for Universal Systems
    Author: Carolina Johnson (CJ), December 2025

    For any prime p >= 11, truncate the rightmost digit and
    find the nearest prime using exactly one binary choice.

    R(p) = k        if k is prime
    R(p) = k + 1    if k is not prime and k+1 is prime
    R(p) = None     otherwise (terminal state)

    Parameters:
    - p: a prime number >= 11

    Returns:
    - next prime in the descent chain, or None if terminal
    """
    if p < 11:
        return None
    k = p // 10
    if isprime(k):
        return k
    elif isprime(k + 1):
        return k + 1
    else:
        return None  # terminal state


def descend(p):
    """
    Follow the full R-chain from p to its terminal state.

    Parameters:
    - p: starting prime >= 11

    Returns:
    - chain: list of primes in the descent sequence
    - terminal: the final state (prime or None for undefined)
    """
    if not isprime(p):
        raise ValueError(f"{p} is not prime.")
    chain = [p]
    current = p
    while True:
        nxt = prime_aware_truncation(current)
        if nxt is None:
            break
        chain.append(nxt)
        current = nxt
    return chain, current


def find_terminal_primes(limit):
    """
    Find all terminal primes up to limit.
    A prime t is terminal if R(t) is undefined.

    Parameters:
    - limit: upper bound for search

    Returns:
    - list of terminal primes
    """
    terminals = []
    p = 11
    from sympy import nextprime
    while p <= limit:
        if prime_aware_truncation(p) is None:
            terminals.append(p)
        p = nextprime(p)
    return terminals


if __name__ == "__main__":
    print("--- THE PRIME-AWARE RIGHT-TRUNCATION OPERATOR ---")
    print("One binary choice. That's all primes need to descend.")
    print()

    # Demonstrate descent chains
    test_primes = [1523, 7331, 9973, 104729, 999983]
    print("Descent chains:")
    for p in test_primes:
        chain, terminal = descend(p)
        print(f"  {p} -> {' -> '.join(str(x) for x in chain)} [terminal: {terminal}]")

    print()

    # Find terminal primes below 1000
    print("Terminal primes below 1000:")
    terminals = find_terminal_primes(1000)
    print(f"  {terminals}")
    print(f"  Count: {len(terminals)}")

    print()
    print("Terminal primes are sparse.")
    print("One degree of freedom is the minimum amount required for stability.")
