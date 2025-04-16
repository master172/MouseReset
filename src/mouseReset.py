import pyautogui
import keyboard
import timer as ti

current_position = None
timeout_started:bool = False
oneshot:bool = True

timer = None

temp_position = None
callback_functions = None

"""
def main_mouse_loop(app):
	check_position()
	app.after(100, lambda: main_mouse_loop(app))
"""

def end_process():
	global timer
	print("ending process")
	del timer

def on_save_mouse_loc():
   global current_position
   current_position = pyautogui.position()
   print("saving current mouse position: "+str(current_position))
   if callback_functions:
	   callback_functions(0)

def on_return_mosuse_loc():
	global current_position
	print("returning mouse position to: "+str(current_position))
	pyautogui.moveTo(current_position)
	if callback_functions():
		callback_functions(1)

"""
def check_position():
	global temp_position
	global timeout_started
	global timer
	global oneshot
	if temp_position != pyautogui.position():
		temp_position = pyautogui.position()
		if timeout_started == True and oneshot == False:
			timeout_started = False
			timer.stop()
	elif temp_position == pyautogui.position():
		if timeout_started == True:
			return
		else:
			timeout_started = True
			timer.start_timer()
			timer.countdown(3)
"""

def start_timer():
	timer.start_timer()
	timer.countdown(1)

def restart_timer():
	timer.stop()
	timer.start_timer()
	timer.countdown(1)

def register_hotkeys():
	keyboard.add_hotkey('ctrl+shift+k', on_save_mouse_loc)
	keyboard.add_hotkey('ctrl+shift+r', on_return_mosuse_loc)

def create_timer(app):
	global timer
	timer = ti.Timer(on_complete=on_save_mouse_loc,callback=app.get_timer_time)

def start(app,callback):
	global callback_functions
	callback_functions = callback
	print("regestring hotkeys and creating timer")
	create_timer(app)
	register_hotkeys()


def start_loop(app):
	start_timer()
	#main_mouse_loop(app)