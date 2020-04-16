class Rotate:
    def __init__(self,arr,d):
        self.arr=arr
        self.d= input('Enter the shift')
        self.n= len(arr)

    def leftrotateone(self):
        self.arr.extend(self.arr[0:self.d])
        del self.arr[0:self.d]
        print(self.arr)

        #temp = self.arr[0]
        #for i in range(self.n-1):
            #self.arr[i]=self.arr[i+1]
        #self.arr[self.n-1]=temp
    
    #def leftrotate(self):
        #for i in range(self.d):
            #leftrotateone()

    #def printArray(self):
        #for i in range(self.n):
            #print(self.arr[i])

__all__ = ['Rotate']





