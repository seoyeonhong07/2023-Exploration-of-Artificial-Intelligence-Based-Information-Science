import time


def time_checker(func):  # closure
    def inner(*args):
        s = time.time()
        r = func(*args)
        e = time.time()
        print(f'총 수행시간은 {e - s}초 입니다')
        return r
    return inner