class Large:
    def __init__(self,arr):
        self.arr = arr
        self.max= arr[0]
        self.n = len(arr)

    def maximum(self):
        
        for i in range(1,self.n):
            if self.arr[i]>self.max:
                self.max=self.arr[i]
        print(self.max)

__all__ = ['Large']