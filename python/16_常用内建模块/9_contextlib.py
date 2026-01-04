

class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


# with Query('Bob') as q:
#     q.query()


from contextlib import contextmanager
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')

with create_query('Bob2') as q:
    q.query()