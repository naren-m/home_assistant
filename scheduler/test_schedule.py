import schedule
import time
import subprocess

import action_part as ap

actions = ap.MyActions()

def job():
	print "i am working"

schedule.every().day.at("06:30").do(actions.play_specified_song)

while True:
	schedule.run_pending()
