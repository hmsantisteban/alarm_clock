from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime
from time import sleep


root = Tk()
root.title("Alarm")
root.geometry('300x150')

frame_line = Frame(root, width=300, height=5, bg='blue')
frame_line.grid(row=0, column=0)

frame_body = Frame(root, width=300, height=295)
frame_body.grid(row=1, column=0)

icon_image = Image.open('icons8-alarmclock.png')
icon_image = ImageTk.PhotoImage(icon_image)

frame_icon = Label(root, image=icon_image)
frame_icon.place(x=10, y=10)

name_title = Label(root, text='Alarm', font='arial 14')
name_title.place(x=90, y=10)

hour_title = Label(root, text='Hour', font='arial 10')
hour_title.place(x=90, y=30)

minutes_title = Label(root, text='Minutes', font='arial 10')
minutes_title.place(x=140, y=30)

ampm_title = Label(root, text='AM/PM', font='arial 10')
ampm_title.place(x=190, y=30)

hour_box = Combobox(root, width=2, font='arial 12')
hour_box['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
hour_box.current(0)
hour_box.place(x=90, y=50)

minute_box = Combobox(root, width=2, font='arial 12')
minute_box['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                        "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",
                        "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
                        "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
minute_box.current(0)
minute_box.place(x=140, y=50)


ampm_box = Combobox(root, width=3, font='arial 12')
ampm_box['values'] = ("AM", "PM")
ampm_box.current(0)
ampm_box.place(x=190, y=50)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    mixer.music.stop()
    root.destroy()


def restart_alarm():
    hour_box.current(0)
    minute_box.current(0)
    ampm_box.current(0)


activate_button = Button(root, font='arial 10', text='Activate Alarm', width=8, command=activate_alarm)
activate_button.place(x=5, y=80)

deactivate_button = Button(root, font='arial 10', text='Deactivate Alarm', width=10, command=deactivate_alarm)
deactivate_button.place(x=90, y=80)

restart_button = Button(root, font='arial 10', text='Restart Alarm', width=8, command=restart_alarm)
restart_button.place(x=190, y=80)


def sound_alarm():
    mixer.music.load('alarm_sound.wav')
    mixer.music.play()


def alarm():
    while True:

        alarm_hour = hour_box.get()
        alarm_minute = minute_box.get()
        alarm_ampm = ampm_box.get()
        alarm_ampm = str(alarm_ampm).upper()

        now = datetime.now()
        print(now)

        hour = now.strftime("%I")
        minutes = now.strftime("%M")
        period_ampm = now.strftime("%p")

        if alarm_ampm == period_ampm:
            if alarm_hour == hour:
                if alarm_minute == minutes:
                    print("Time to take a break!")
                    sound_alarm()
        sleep(1)


mixer.init()
root.mainloop()
