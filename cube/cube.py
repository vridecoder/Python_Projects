class Cube:
    def __init__(self, n):
        self.input = n
        self.sum = 0
        self.result = 0
    def cubesum(self):
        self.sum = (self.input*(self.input+1)/2)
        self.result = (self.sum * self.sum)
        print(self.result)

__all__ = ['Cube']