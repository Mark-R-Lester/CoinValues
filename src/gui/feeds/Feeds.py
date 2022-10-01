
from time import strftime, gmtime, sleep
import threading
from PyQt6.QtCore import QObject, pyqtSignal

from src.feeds.FixedSupplyCoinFeed import FixedSupplyCoinFeed


class Feeds(QObject):
    
    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(list, arguments=['emitCoins'])

    def emit_coins(self, coins):
        self.updated.emit(coins)

    def stream(self):

        def fixed_supply_stream():
            feed = FixedSupplyCoinFeed().feed()
            while True:
                for coins in feed:
                    self.emit_coins(coins)
       
        thread = threading.Thread(target=fixed_supply_stream)
        thread.daemon = True
        thread.start()