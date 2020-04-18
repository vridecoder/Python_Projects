from sortrecur import Sortrecur
if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7]

    sortrecur=Sortrecur(arr)
    if sortrecur.sort(arr) == True:
        print("Yes")
    else:
        print("No")