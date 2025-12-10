from inspect import stack


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer')
        if score < 0 or score > 100:
            raise ValueError('score must be between 0 and 100')
        self._score = score


    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2025 - self._birth

    def __str__(self):
        return 'Student object (birth:%s, score:%s)' % (self.birth, self.score)


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L




class Student2(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'sore':
            return 99
        raise AttributeError('\'Student2\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        print('My name is %s.' % self.name)



from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6



class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)

