import webbrowser
import subprocess
import os
from datetime import datetime

import app_logger

logger = app_logger.logger

#http://www.valmiki.iitk.ac.in/content?field_kanda_tid=1&language=dv&field_sarga_value=1&field_sloka_value=1
# /home/narenuday/Music/songs/Yenduko.mp3
class MyActions:

	def open_google(self):
		print "opening google"
		webbrowser.open("http://www.google.com")

	def open_outlook(self):
		print "in open outlook"
		subprocess.call('open -a Microsoft\ Outlook', shell = True)

	def play_youtube_playlist(self):
		print "Playing youtube song"
		webbrowser.open("https://www.youtube.com/watch?v=8gneYVF8RPY")

	def play_specified_song(self):
		print "Playing scheduled song @", datetime.now().time().strftime('%l:%M%p %Z on %b %d, %Y')
		song_play_cmd = "(sleep 1 ; play -q /home/narenuday/Music/songs_with_folders/devotional/suprabatham_mss.mp3 ) &"
		# song_play_cmd = "(sleep 1 ; play -q /home/narenuday/Music/songs/Yenduko.mp3 ) &"
		logger.info("Executing command %s", song_play_cmd)
		print song_play_cmd
		os.system(song_play_cmd)


if __name__ == '__main__':
	myAction = MyActions()
	myAction.open_google()