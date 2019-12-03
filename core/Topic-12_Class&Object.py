#Use Pascal naming convention for declaring class Names.
class Point:

    def move(self):
        print("Move")

    def draw(self):
        print('Draw')


point1=Point()
point1.draw()
point1.move()
point1.x=10
point1.y=20
print(f'{point1.x,point1.y}')
