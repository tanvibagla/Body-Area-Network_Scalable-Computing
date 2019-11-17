import time, threading
def foo(number):
    print(number)
    threading.Timer(number, foo, args=[number]).start()

foo(5)
foo(10)