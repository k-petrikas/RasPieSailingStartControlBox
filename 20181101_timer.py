import time
import datetime
import timeit


def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_second_later = datetime.timedelta(seconds=1)
    for remaining in range(x, 0, -1):
        target += one_second_later
        print(datetime.timedelta(seconds=remaining), '\r')
        time.sleep((target - now()).total_seconds())
    print('\nTIMER ended')


if __name__ == '__main__':
    print(timeit.timeit(lambda:countdown_timer(120), number=1))
