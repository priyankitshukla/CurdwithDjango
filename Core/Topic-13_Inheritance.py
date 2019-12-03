class Mamal:
    def walk(self):
        print('Walk')


class Dog(Mamal):
    pass

class Cat(Mamal):
    pass


dog = Dog();
dog.walk()
cat = Cat()
cat.walk()