import time
import timeit
import datetime
import winsound
import threading 
import multiprocessing


s = 5

def time_keeper(sequence_length):

    three_min_sequence = [[0,[3,0]],[60,[2,0]],[30,[1,3]],[30,[1,0]],[30,[0,3]],[10,[0,2]],[10,[0,1]],[5,[0,1]],[1,[0,1]],[1,[0,1]],[1,[0,1]],[1,[0,1]],[1,[0,1]]]
    five_min_sequence = [[0,[1,0]],[60,[1,0]],[180,[1,0]],[60,[1,0]]]
##    for x in five_min_sequence:
    for x in three_min_sequence:
        print(x)
        time.sleep(x[0])

        long_horn_count = x[1][0]
        short_horn_count = x[1][1]
        t = threading.Thread(target=horn_check_thread, args=(long_horn_count, short_horn_count))
        t.start()
 




    return;

def horn_check_thread(long_horn_count, short_horn_count):
    if (long_horn_count > 0) :
        i = 1
        while i <= long_horn_count:
            long_horn()
            i += 1

    if (short_horn_count > 0) :
        i = 1
        while i <= short_horn_count:
            short_horn()
            i += 1


   

def long_horn():
    winsound.Beep(1000, 1000)
    return;

def short_horn():
    winsound.Beep(1000, 500)
    return;

if __name__ == '__main__':
    print(timeit.timeit(lambda:time_keeper(s), number=1))
    print("DONE")






