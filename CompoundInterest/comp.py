class Compound:
    def __init__(self, p, r, t):
        self.principal = p
        self.rate = r
        self.time = t
        self.ci = 0

    def output(self):
        self.ci = self.principal * (pow((1+self.rate/100), self.time))
        print("The Compund Interest is", self.ci)


__all__ = ['Compound']

    