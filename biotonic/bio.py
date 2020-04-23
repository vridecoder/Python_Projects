class Bio:
    def __init__(self, arr):
        self.arr=arr
        self.n= len(arr)

    def checkbiotonic(self):
        for i in range(1,self.n):
            if self.arr[i]>self.arr[i-1]:
                continue
            else:
                break

        if i == self.n-1:
            return True

        for j in range(i+1,self.n):
            if self.arr[j]<self.arr[j-1]:
                continue
            else:
                break
        i = j
        if i != self.n-1:
            return False
        return True

__all__ = ['Bio']