import time
from progressbar import *

total = 100


def dowork():
    time.sleep(0.1)


widgets = ['Progress: ', Percentage(), ' ', Bar('#'), ' ', Timer(), ' ', ETA(), ' ', FileTransferSpeed()]
bar = ProgressBar(widgets=widgets, maxval=total)
bar.start()
for i in range(total):
    bar.update(i + 1)
    dowork()
bar.finish()
