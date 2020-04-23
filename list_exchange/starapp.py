class Star:
    def __init__(self):
        self.n=0

    def swaplist(self,listlen):
        start, *middle, end = listlen
        listlen = end, *middle, start

        return listlen

__all__ = ['Star']