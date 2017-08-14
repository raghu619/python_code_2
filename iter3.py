from collections import namedtuple
Point = namedtuple('Point','x,y')
car=namedtuple("Car","Price ,Mileage, Colour ,Class")
xyz = car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(pt1)
print(dot_product)
print(xyz.Price)   
from collections import namedtuple
N = int(input());student = namedtuple('student',input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for i in range(N))/N)







