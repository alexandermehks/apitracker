from datetime import datetime

def do_log(text): 
	time = datetime.now().strftime("%H:%M:%S")
	date = datetime.now().date()
	with open("logFile.txt", "a") as file:
		file.write(f"{date} {time} {text}\n")
		file.close()