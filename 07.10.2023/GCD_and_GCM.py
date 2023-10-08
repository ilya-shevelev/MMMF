class Solution:
    def __init__(self, a: int, b: int) -> None:
        self.a, self.b = max(a, b), min(a, b)

    def __call__(self) -> str:
        return f'НОД({self.a}, {self.b})={self.get_GCD()}, НОК({self.a}, {self.b})={self.get_GCM()}'

    def get_GCD(self) -> int:
        c = self.a % self.b
        while True:
            if not self.b % c:
                return c
            c = self.b % c

    def get_GCM(self) -> int:
        return int(self.a * self.b / self.get_GCD()) # НОК(A) * НОД(B) = A * B


if __name__ == '__main__':
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(Solution(a, b)())
    input()
