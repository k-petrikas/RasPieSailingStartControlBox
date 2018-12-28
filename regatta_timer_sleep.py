import time
import timeit
import datetime
import winsound
import threading 

s = 5

def time_keeper(sequence_length):

    three_min_sequence = [[60,[2,0]],[30,[1,3]],[30,[1,0]],[30,[0,3]],[10,[0,2]],[10,[0,1]],[5,[0,1]],[1,[0,1]],[1,[0,1]],[1,[0,1]],[1,[0,1]],[1,[0,1]]]
    print("start")
    for x in three_min_sequence:
        print(x)
        time.sleep(x[0])
        print("slept")
        print(x[1][0])
        print(x[1][1])
      
        if (x[1][0] > 0) :
            print("long horn " , x[1][0])
            #TODO: switch to variable
        if (x[1][1] > 0) :
            print("short horn " , x[1][1])
    
    print("DONE")




    return;

def horn_check_thread(type_of_start, seconds_remaining):
    if (seconds_remaining == 4 ) :
            print( '3S Horn: ', seconds_remaining ) 
            threading.Thread(target=sound_horn).start()
    if (seconds_remaining == 2 ) :
            print( '2S Horn: ', seconds_remaining ) 
            threading.Thread(target=sound_horn).start()

   

def sound_horn():
    print ("BEEP")
    winsound.Beep(2000, 1000)
    return;

if __name__ == '__main__':
    print(timeit.timeit(lambda:time_keeper(s), number=1))





