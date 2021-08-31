import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
	window.after_cancel(timer)
	timer_label.config(text='Timer', fg=GREEN)
	canvas.itemconfig(timer_text, text='00:00')
	check_label['text'] = ''
	global reps
	reps = 0
	

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
	global reps
	work_sec = WORK_MIN * 60
	short_break = SHORT_BREAK_MIN * 60
	long_break = LONG_BREAK_MIN * 60
		
	# work_sec = 3
	# short_break = 1
	# long_break = 2
	#
	reps += 1
	if reps % 2 != 0 and reps != 8:
		count_down(work_sec)
		timer_label['text'] = 'Work'
		timer_label['fg'] = GREEN
	elif reps % 2 == 0 and reps != 8:
		count_down(short_break)
		timer_label['text'] = 'Break'
		timer_label['fg'] = PINK
		# check_label['text'] += '✔'
	elif reps == 8:
		count_down(long_break)
		timer_label['text'] = 'Break'
		timer_label['fg'] = RED


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
	minute = math.floor(count / 60)
	seconds = count - minute * 60
	if minute < 10:
		minute = f'0{minute}'
	if seconds < 10:
		canvas.itemconfig(timer_text, text=f'{minute}:0{seconds}')
	else:
		canvas.itemconfig(timer_text, text=f'{minute}:{seconds}')
	if count >= 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		if reps % 9 == 0:
			check_label['text'] = ''
		elif reps % 2 == 0:
			check_label['text'] += '✔'

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text='00:00', font=('Book Antiqua', 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)

timer_label = tk.Label(text='Timer', font=('Book Antiqua', 40, 'normal'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = tk.Label(text='', font=('Book Antiqua', 20, 'normal'), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = tk.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
