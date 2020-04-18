class Sortrecur:
    def __init__(self,numbers):
        self.data=numbers
        self.n=len(numbers)

    def sort(self,arr):
        l=len(arr)

        if l==1 or l==0:
            return True

        return arr[0]<=arr[1] and self.sort(arr[1:])

__all__ = ['Sortrecur']

