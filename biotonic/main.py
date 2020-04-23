from bio import Bio
if __name__ == "__main__":
    arr = [-3,9,7,20,17,5,1]
    #arr=[1,2,3,4,5,6,7]
    n = len(arr)

    bio=Bio(arr)
    if bio.checkbiotonic() == True:
        print("Yes")
    else:
        print("No")
