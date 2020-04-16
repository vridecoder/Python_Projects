class Split:
    def __init__(self,arr):
        self.arr=arr
        self.k=input('Enter the split index:')
        self.n= len(arr)
        self.e=0
        self.f=0
        self.g=0

    def splitadd(self):
        self.e=self.arr[:self.k]
        self.f=self.arr[self.k:]
        self.g=self.f+self.e
        print(self.g)
        #print(self.e)
        

__all__ = ['Split']
