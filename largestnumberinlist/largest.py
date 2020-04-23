class Large:
    def __init__(self, list1, n):
        self.list1=list1
        self.n = n

    def find_largest(self):
        final_list=[]
        for i in range(0,self.n):
            max1=0

            for j in range(len(self.list1)):
                if self.list1[j]>max1:
                    max1=self.list1[j]

            self.list1.remove(max1)
            final_list.append(max1)
        print(final_list)

__all__=['Large']