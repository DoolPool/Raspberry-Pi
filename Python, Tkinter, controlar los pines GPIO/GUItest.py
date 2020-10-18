import Tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO21 = 21
GPIO20 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)

master = tk.Tk()
master.title("GPIO Control")
master.geometry("300x100")

GPIO21_state = True
GPIO20_State = True

def GPIO21button():
	global GPIO21_state
	if GPIO21_state == True:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = False
		ONlabel = tk.Label(master, text="Turned ON", fg="green")
		ONlabel.grid(row=0, column=1)
	else:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = True
		ONlabel = tk.Label(master, text="Turned OFF", fg="red")
		ONlabel.grid(row=0, column=1)


def GPIO20button():
	global GPIO20_State
	if GPIO20_State == True:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = False
		OFFlabel = tk.Label(master, text="Turned ON", fg="green")
		OFFlabel.grid(row=1, column=1)
	else:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = True
		OFFlabel = tk.Label(master, text="Turned OFF", fg="red")
		OFFlabel.grid(row=1, column=1)

ONbutton = tk.Button(master, text="GPIO 21", bg="blue", command=GPIO21button)
ONbutton.grid(row=0, column=0)

OFFbutton = tk.Button(master, text="GPIO 20",bg="blue" , command=GPIO20button)
OFFbutton.grid(row=1, column=0)

Exitbutton = tk.Button(master, text="Exit",bg="red", command=master.destroy)
Exitbutton.grid(row=2, column=0)
master.mainloop()
