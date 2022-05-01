from datetime import datetime
from inspect import currentframe
import os

def do_log(text): 
	current = os.getcwd()
	os.chdir("../logs")
	time = datetime.now().strftime("%H:%M:%S")
	date = datetime.now().date()
	with open("logFile.txt", "a") as file:
		file.write(f"{date} {time} {text}\n")
		file.close()
	os.chdir(current)

def log_error(text, row):
	current = os.getcwd()
	os.chdir("../logs")
	time = datetime.now().strftime("%H:%M:%S")
	date = datetime.now().date()
	with open("error-log.txt", "a") as file:
		file.write(f"{date} {time} {text} ROW:{row}\n")
		file.close()
	os.chdir(current)

def get_row():
	cf = currentframe()
	return cf.f_back.f_lineno
