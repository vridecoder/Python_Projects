from palin import Palin
if __name__=='__main__':
    inputs = [ 
    [3,2,0,2,3],
    [1,2,3,4,5],
    [2,3,4,3,2]]
    for arr in inputs:
        n=len(arr)
        palin=Palin(arr)
        if (palin.palindrome(arr,0,n-1)==1):
            print("Palindrome")
        else:
            print("Not Palindrome")
