import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(d):
        return {'name': d.name, 'age': d.age, 'score': d.score}

def dict2student(d):
        return Student(d['name'], d['age'], d['score'])
