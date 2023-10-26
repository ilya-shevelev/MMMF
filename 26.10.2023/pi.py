def calculate_pi() -> float:
    """
    1/1 + 1/4 + 1/9 + 1/16 + 1/25 + ... = (pi^2)/6
    """
    a = sum(1 / (i ** 2) for i in range(1, 10_000_000))
    print(pow(a * 6, .5))

calculate_pi()
