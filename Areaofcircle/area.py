class Area:
    def __init__(self, r):
        self.rad = r
        self.area = 0

    def areacircle(self):
        self.area = 3.14 * pow(self.rad,2)
        print("The area of circle is",self.area)

__all__ = ['Area']