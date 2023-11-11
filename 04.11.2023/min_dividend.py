def min_dividend(values: dict[int, int]) -> int:
    dividend = None
    attempt = 1
    while not dividend:
        if all(attempt % divider == remainder for divider, remainder in values.items()):
            dividend = attempt
        else:
            attempt += 1
    print(dividend)
