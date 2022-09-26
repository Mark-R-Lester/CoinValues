
from time import strftime, gmtime, sleep
import threading
from PyQt6.QtCore import QObject, pyqtSignal

from src.feeds.CoinFeed import CoinFeed


class MainCoinFeed(QObject):
    
    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(list, arguments=['emitCoins'])

    def emit_coins(self, coins):
        self.updated.emit(coins)

    def stream(self):
        thread = threading.Thread(target=self._stream)
        thread.daemon = True
        thread.start()

    def _stream(self):
        feed = CoinFeed().feed()
        while True:
            for coins in feed:
                self.emit_coins(coins)
       