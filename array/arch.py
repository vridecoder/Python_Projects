class Array:
    def __init__(self,arr, sum):
        self.arr = arr
        self.sum = 0
        self.n = len(arr)

    def subArray(self):
        for i in range(self.n):
            cur_sum = self.arr[i]
            j = i+1
            while j <=self.n:
                if cur_sum == self.sum:
                    print("Sum found between")
                    print("indexes",(i, j-1))
                    return 1
                if cur_sum > sum or j==self.n:
                    break
                cur_sum = cur_sum + self.arr[j]
                j = j+1

        print("No Subarray found")
        return 0


