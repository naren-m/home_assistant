import schedule
import time
import action_part as ap
import subprocess

actions = ap.MyActions()
actions.open_google()
# actions.open_outlook()


def job():
	print "i am working"

schedule.every().day.at("22:36").do(actions.open_google)

while True:
	schedule.run_pending()