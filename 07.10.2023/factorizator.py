class Solution:
    def __init__(self, num: int) -> None:
        self.num = num
        self.set_primes()

    def set_primes(self) -> None:  # sieve of Eratosthenes
        number_row = list(range(2, self.num + 1))
        for i in number_row:
            for j in number_row[number_row.index(i) + 1:]:
                if j % i == 0:
                    number_row.remove(j)
        self.primes = number_row

    def factorize(self) -> str:
        num = self.num
        if num == 1:
            prime_divisors = [1]
        elif not num == int(num):
            raise TypeError('Number should be an integer.')
        elif num < 1:
            raise TypeError('Number should be natural.')
        else:
            prime_divisors = []
            while num != 1:
                for divisor in self.primes:
                    if num % divisor == 0:
                        prime_divisors.append(divisor)
                        num /= divisor
        result = f'{self.num} = {" * ".join(str(i) for i in prime_divisors)}'
        return result

if __name__ == '__main__':
    num = int(input('Type natural number: '))
    print(Solution(num).factorize())
    input()
