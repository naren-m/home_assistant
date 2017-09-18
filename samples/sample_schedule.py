import schedule
import time

import actions

a = actions.Actions()
a.open_google()
# schedule.every(1).minutes.do(a.open_google)


# while True:
#     schedule.run_pending()
