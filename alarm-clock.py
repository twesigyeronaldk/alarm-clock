import time
import datetime
import tkinter as tk
from playsound import playsound

root = tk.Tk()
root.geometry("500x200")
root.title("KIA Alarm Clock")

hour_var = tk.StringVar()
minutes_var = tk.StringVar()
seconds_var = tk.StringVar()

msg_var = tk.StringVar()

def set_alarm():
    hour = hour_var.get()
    minutes = minutes_var.get()
    seconds = seconds_var.get()

    # make sure all entries are numeric
    if hour.isnumeric() and minutes.isnumeric() and seconds.isnumeric():

        while True:

            time.sleep(1)
            
            current_hour = datetime.datetime.now().hour
            current_minutes = datetime.datetime.now().minute
            current_seconds = datetime.datetime.now().second

            if current_hour == int(hour) and current_minutes == int(minutes) and current_seconds == int(seconds):
                msg_var.set("Time to wake up.")
                playsound('./ALARM.WAV')
                break
    else:
        msg_var.set("Please submit only numeric data. Thank you.")
     
    hour_var.set("")
    minutes_var.set("")
    seconds_var.set("")

label1 = tk.Label(root, text="Alarm Time", font=("Arial", 18))
label1.pack(padx=10, pady=10)

label2 = tk.Label(root, text="Alarm time must be in twenty four (24) hour clock.", font=("Arial", 10))
label2.pack(padx=5, pady=5)

# textbox = tk.Text(root, height=1, font=("Arial", 16))
# textbox.pack(padx=20, pady=20)

# entry = tk.Entry(root)
# entry.pack(padx=10, pady=10)

frame1 = tk.Frame(root)
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)

entry1 = tk.Entry(frame1, textvariable=hour_var)
entry1.grid(row=0, column=0, sticky=tk.W+tk.E)

entry2 = tk.Entry(frame1, textvariable=minutes_var)
entry2.grid(row=0, column=1, sticky=tk.W+tk.E)

entry3 = tk.Entry(frame1, textvariable=seconds_var)
entry3.grid(row=0, column=2, sticky=tk.W+tk.E)

frame1.pack(fill='x')

button = tk.Button(root, text="Submit", font=("Arial", 12), command=set_alarm)
button.pack(padx=10, pady=10)

label3 = tk.Label(root, text="", textvariable=msg_var, font=("Arial", 10), background="#f00")
label3.pack(padx=5, pady=5)

root.mainloop()