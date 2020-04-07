class Factorial:
    def __init__(self, n):
        self.num = n
        self.fact = 1
    
    def factorial(self):
        for i in range(1, self.num+1):
            self.fact= self.fact*i

        print(self.fact)

__all__ = ['Factorial']