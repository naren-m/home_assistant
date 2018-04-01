#!/usr/bin/env python

# Source url http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/

import sys
from daemon import Daemon
import sched, time
from action_part import MyActions

s = sched.scheduler(time.time, time.sleep)

priority = 1
one_minute = 60 

class MyDaemon(Daemon):
	def run(self):
		s.enter(1, 1, do_something, (s,))
		s.run()

my_actions = MyActions()

class EmailCheckDaemon(Daemon):
	def __init__(self, *args, **kwargs):
		Daemon.__init__(self,kwargs['pidfile'])
		self._minutes = kwargs['minutes']
		self._actions = kwargs['actions']
		print "in email_check_daemon.py EmailCheckDaemon self._minutes", self._minutes
		print "in email_check_daemon.py EmailCheckDaemon self._actions", self._actions

	def _setup_action(self):
		my_actions.open_google()
		sc.enter(one_minute, priority, do_something, (sc,))

	def run(self):
		time_interval = 1 * one_minute
		s.enter(time_interval, priority, self._setup_action(), (s,))
		s.enter()

if __name__ == "__main__":
	# my_actions = MyActions()
	email_check_daemon = EmailCheckDaemon(pidfile ='/tmp/email_check_daemon.pid', minutes = 1, actions=my_actions)
	
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			email_check_daemon.start()
		elif 'stop' == sys.argv[1]:
			email_check_daemon.stop()
		elif 'restart' == sys.argv[1]:
			email_check_daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)