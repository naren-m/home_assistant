import schedule
import time
import subprocess
import webbrowser


def open_google():
    """
    Opens google in the default browser

    :rtype: bool

    """
    webpage = 'http://www.google.com'
    retval = webbrowser.open(webpage)

    return retval


schedule.every(1).minutes.do(open_google)

while True:
    schedule.run_pending()
    time.sleep(1)
