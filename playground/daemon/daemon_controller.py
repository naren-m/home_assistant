#!/usr/bin/env python

import sys, time
from daemon import Daemon
import action_part as ap

import schedule

try:
	actions = ap.MyActions()
except Exception, e:
	print "Exception, ", e
	raise


class MyDaemon(Daemon):
	def run(self):
		try:
			schedule.every(1).minutes.do(actions.play_youtube_playlist)
		except Exception, e:
			print "Exception in MyDaemon run", e
			raise

		while True:
			schedule.run_pending()


if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
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