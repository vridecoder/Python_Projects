class Palin:
    def __init__(self,numbers):
        self.data=numbers
        self.length=len(numbers)
        #self.arr=arr
        #self.begin=begin
        #self.end=end

    def palindrome(self,arr,begin,end):
        if (begin>=end):
            return True

        if (arr[begin]==arr[end]):
            return self.palindrome(arr,begin+1,end-1)
        else:
            return 0

__all__ = ['Palin']

            