
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score) )


    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('score must be between 0 and 100')

    def set_name(self, name):
        self.__name = name




# bart = Student('Bart', 80)
# lisa = Student('Lisa', 70)
# bart.print_score()
# lisa.print_score()


#继承和多态

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')



# dog  = Dog()
# cat = Cat()
# dog.run()
# cat.run()
# dog.eat()


class Timer(object):
    def run(self):
        print('Timer is running...')


def run_twice(animal):
    animal.run()
    animal.run()


# run_twice(Dog())
# run_twice(Cat())
# run_twice(Timer())

#获取对象信息




















