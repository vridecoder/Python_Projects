class Arm:
    def __init__(self, n):
        self.num = n
        self.order = len(str(self.num))
        self.sum = 0
        self.temp = 0
        self.digit = 0

    def arms(self):
        self.temp = self.num
        while self.temp > 0:
            self.digit = self.temp%10
            self.sum = self.sum + self.digit ** self.order
            self.temp //= 10

        if self.num == self.sum:
            print(self.num, "is an Armstrong number")
        else:
            print(self.num,"is not an Armstrong number")


__all__ = ['Arm']
