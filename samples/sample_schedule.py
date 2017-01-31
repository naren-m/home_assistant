import schedule
import time
import subprocess

import actions

a = actions.Actions()

schedule.every(1).minutes.do(a.open_google)

while True:
	schedule.run_pending()
