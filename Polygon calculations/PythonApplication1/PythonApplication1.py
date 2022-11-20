class Polygon:
    def __init__(self,side,length,breadth,radius):
        self.side=side
        self.length=length 
        self.breadth=breadth
        self.radius=radius
    def square(self):
        area=self.side**2
        return area
    def rectangle(self):
        area=self.length*self.breadth
        return area
    def circle(self):
        area=self.radius*2
        return area
area1 = Polygon(2,3,4,5)
print(area1.square())
print(area1.rectangle())
print(area1.circle())