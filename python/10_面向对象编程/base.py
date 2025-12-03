
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score) )



# bart = Student('Bart', 80)
# lisa = Student('Lisa', 70)
# bart.print_score()
# lisa.print_score()
