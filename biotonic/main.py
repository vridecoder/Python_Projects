from bio import Bio
if __name__ == "__main__":
    arr = [-3,9,7,20,17,5,1]
    #arr=[1,2,3,4,5,6,7]
    n = len(arr)

    bio=Bio(arr)
    for i in range(1,n):
        if bio.checkbiotonic() == 1:
            print("Yes")
        else:
            print("No")
