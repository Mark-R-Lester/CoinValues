
from time import strftime, gmtime, sleep
import threading
from PyQt6.QtCore import QObject, pyqtSignal

class Clock(QObject):
    '''Supplies the time to the gui '''

    def __init__(self):
        '''Constructor that creates the Qobject'''
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['tick'])

    def tick(self):
        '''Gets the present time and emits it to the gui'''
        curr_time = strftime("%H:%M:%S", gmtime())
        self.updated.emit(curr_time)

    def start(self):
        '''Creates a therad for the clock to run on'''
        t_thread = threading.Thread(target=self._start)
        t_thread.daemon = True
        t_thread.start()

    def _start(self):
        '''Starts the clock and makes it tick every 10th of a second'''
        while True:
            self.tick()
            sleep(0.1)