#alarm clock with python

from tkinter import*
import datetime
import time
import winsound
#set_alarm_timer = input('enter time to wake up:')
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datatime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d:%m:%y")
        print('the set date is:', date)
        print(now)
        if now == set_alarm_timer:
            print('TIME TO WAKE UP')
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f'{hour.get()}:{min.get()}:{sec.get()}'
    alarm(set_alarm_timer)
