from datetime import datetime
from inspect import currentframe

def do_log(text): 
	time = datetime.now().strftime("%H:%M:%S")
	date = datetime.now().date()
	with open("logs/logFile.txt", "a") as file:
		file.write(f"{date} {time} {text}\n")
		file.close()

def log_error(text, row):
	time = datetime.now().strftime("%H:%M:%S")
	date = datetime.now().date()
	with open("logs/error-log.txt", "a") as file:
		file.write(f"{date} {time} {text} ROW:{row}\n")
		file.close()

def get_row():
	cf = currentframe()
	return cf.f_back.f_lineno
