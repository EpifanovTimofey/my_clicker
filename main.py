import time

import model
import view
import control
while True:
    time.sleep(1/60)
    view.main_view()
    control.p()
