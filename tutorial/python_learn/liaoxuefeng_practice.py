# ------------------------ day01


#------------------------ day02

'''
def fib(n):
    k = 0
    a , b = 0, 1
    while k < n:
        k += 1
        yield a
        a, b = b ,a+b

for i in fib(5):
    print(i)


'''
'''
def grep(pattern):
    print("search for",pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
search.send('i love coroutine')
search.close
'''
'''
def consumer():
    r = ''
    while True:
        print("2")
        n = yield r
        print('r is : %s' % r)
        print("4")
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print("1")
    c.send(None)
    print("3")
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

'''
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('--------1-------- (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('--------2-------- (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('--------3-------- (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()