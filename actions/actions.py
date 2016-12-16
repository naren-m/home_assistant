import webbrowser
import subprocess

#http://www.valmiki.iitk.ac.in/content?field_kanda_tid=1&language=dv&field_sarga_value=1&field_sloka_value=1

# with open("test.txt", "a") as myfile:
# 	myfile.write("number")

class Actions:

	def open_google(self):
		print "opening google"
		webbrowser.open("http://www.google.com")

	def open_outlook(self):
		print "in open outlook"
		subprocess.call('open -a Microsoft\ Outlook', shell = True)

	def play_youtube_playlist(self):
		print "Playing youtube song"
		webbrowser.open("https://www.youtube.com/watch?v=8gneYVF8RPY")

if __name__ == '__main__':
	myAction = Actions()
	myAction.open_google()
