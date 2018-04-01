#!/usr/bin/env python

# Source url http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/

import sys
from daemon import Daemon
import action_part as ap
import schedule


class MyDaemon(Daemon):
	def run(self):
		print "in MyDaemon run"
		try:
			actions = ap.MyActions()
			schedule.every(1).minutes.do(actions.open_google)
		except Exception as e:
			print str(e)
			sys.exit(2)

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
	print "main"

	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			print "start"
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