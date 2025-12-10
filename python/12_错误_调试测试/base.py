import logging

def tryTest():
    try:
        print('try ...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('got exception:', e)
        logging.exception(e)
    finally:
        print('finally...')
    print('end')

tryTest()