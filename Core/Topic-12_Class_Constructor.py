#Use Pascal naming convention for declaring class Names.
# for constructor use def __init__(self)
class Point:

     def __init__(self,x,y):
         self.x=x
         self.y=y

     def move(self):
         print("Move")

     def draw(self):
         print('Draw')


point=Point(10,20)
print(point.x)


## Excersize


class Person:
    def __init__(self,name):
        self.name=name

    def talk(self,name):
        print(f'{name} is talking currently')

#name=
person=Person(input("Enter name"))
person.talk(person.name)