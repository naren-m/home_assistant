import pyttsx
# for v in ['english', 'english-us', 'english-north', 'english_rp', 'english_wmids']:
v = 'english-us'

class Speak(object):
	"""docstring for SpeakUtils"""		
	def say(self, sentence):
		engine = pyttsx.init()
		engine.setProperty('voice', v)	
		engine.say(sentence)
		engine.runAndWait()
