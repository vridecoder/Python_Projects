class Mono:
    def __init__(self,arr):
        self.arr=arr
        self.n=len(arr)

    def isMono(self):
        print (all(self.arr[i] <= self.arr[i+1] for i in range(self.n-1)) or all(self.arr[i] >= self.arr[i+1] for i in range(self.n-1)))

    #def call_isMono(self):
        #print(isMono, self.arr)

__all__ = ['Mono']
            