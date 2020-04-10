class Sqr:
    def __init__(self, n):
        self.input = n
        self.sum = 0
        #len(self.input)

    def square(self):
        for i in range(1,(self.input+1)):
            self.sum = self.sum + (i*i)
        print(self.sum)

__all__ = ['Sqr']
