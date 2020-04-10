class Array:
    def __init__(self, arr, n):
        self.arr = []
        self.n = len(arr)
        self.sum = 0

    def sum(self):
        for i in range(0,self.n):
        self.sum = (self.sum + self.arr[i])
        print(str(self.sum))

__all__ = ['Array']

