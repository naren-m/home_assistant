#!/usr/bin/env python

import sys, time
import action_part as ap
import logging
import pyttsx, time
import schedule
import app_logger

from daemon import Daemon

logger = app_logger.logger

engine = pyttsx.init()

# https://github.com/dbader/schedule

try:
	actions = ap.MyActions()
except Exception, e:
	print "Exception, ", e
	raise


class MyDaemon(Daemon):
	def run(self):
		try:
			scheduled_time = "07:00"
			schedule.every().day.at(scheduled_time).do(actions.play_specified_song)
			logger.info("Playing at %s", time)
		except Exception, e:
			logger.error("Exception in MyDaemon run", e)
			raise

		while True:
			schedule.run_pending()
			time.sleep(1)
			# engine.say('Naren')
			# engine.runAndWait()


if __name__ == "__main__":
	file_name = '/tmp/daemon-music.pid'
	daemon = MyDaemon(file_name)
	logger.info("Started daemon process, pid stored in %s", file_name)
	
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
