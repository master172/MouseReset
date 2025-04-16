import time

class TimerError(Exception):

	def __init__(self, message=None, *, start_time=None, end_time=None):
		if message is None:
			message = "an error occured with the timer"
		super().__init__(message)
		self.start_time = start_time
		self.end_time = end_time

	def __str__(self):
		base_message = super.__str__()
		details = []
		if self.start_time is not None:
			details.append(f"start time: {self.start_time}")
		if self.end_time is not None:
			details.append(f"end time {self.end_time}")
		if details:
			return f"{base_message} ({', '.join(details)})"
		return base_message

class Timer:
	
	def __init__(self, on_complete=None,callback=None):
		self.start_time = None
		self.on_complete = on_complete
		self.callback = callback
		print("timer is being created")
		
	def __del__(self):
		print("timer is being destroyed")

	def start_timer(self):
		if self.start_time is not None:
			raise TimerError("Timer is already running.", start_time=self.start_time)
		print("timer started")
		self.start_time = time.perf_counter()
		self.stop_countown = False

	def stop(self):
		if self.start_time is None:
			raise TimerError("Timer is not running. Use .start() to start it.")
		print("timer stopped")
		elpased_time = time.perf_counter() -self.start_time
		self.start_time = None
		self.stop_countown = True
		return elpased_time

	def countdown(self,seconds:int):
		print(f"Starting countdown for {seconds} seconds:")
		while seconds > 0:
			if self.stop_countown == True:
				break
			mins, secs = divmod(seconds,60)
			if self.callback:
				self.callback(f"{mins:02}:{secs:02}")
			print(f"{mins:02}:{secs:02}", end="\r")
			
			time.sleep(1)
			seconds -= 1
		
		if self.stop_countown == True:
			return
		
		print("Time's up!")
		if self.callback:
			self.callback("position saved")
		if self.on_complete:
			self.on_complete()