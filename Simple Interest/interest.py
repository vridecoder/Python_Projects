class SI:
    def __init__(self, p, r, t):
        self.principal = p
        self.rate = r
        self.time = t
        self.result = 0
        self.out = 0

    def interestout(self):
        self.result = self.principal * self.rate * self.time 
        self.out = (self.result)/100
        #print(self.result)
        print("The simple interest is", self.out)

__all__ = ['SI']