import time
import datetime
import timeit


def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_second_later = datetime.timedelta(seconds=1)
    for remaining in range(x, 0, -1):
        target += one_second_later
        print(datetime.timedelta(seconds=remaining-1), 'remaining', end='\n')
        time.sleep((target - now()).total_seconds())
        if ( remaining == 195 ) : print( 'warning Horn', remaining )
        if ( remaining == 180 ) : print( '3M Horn', remaining )
        if ( remaining == 120 ) : print( '2M Horn', remaining )
        if ( remaining == 90 ) : print( ' 1:30 Horn', remaining )
        if ( remaining == 60 ) : print( '1M Horn', remaining )
        if ( remaining == 30 ) : print( '3 Short Horns', remaining )
        if ( remaining == 10 ) : print( 'Count down Horns start', remaining )
        if ( remaining == 5 ) : print( '5S Horn', remaining )
        if ( remaining == 0 ) : print( 'Start', remaining )

if __name__ == '__main__':
    print(timeit.timeit(lambda:countdown_timer(195), number=1))
