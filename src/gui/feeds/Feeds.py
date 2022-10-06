
from time import strftime, gmtime, sleep
import threading
from PyQt6.QtCore import QObject, pyqtSignal

from src.feeds.FixedSupplyCoinFeed import FixedSupplyCoinFeed
from src.feeds.TickersFeed import TickersFeed


class Feeds(QObject):
    
    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(list, arguments=['emitCoins'])
    updatedTickers = pyqtSignal(list, arguments=['emitTickers'])

    def emit_coins(self, coins):
        self.updated.emit(coins)

    def emit_tickers(self, tickers):
        self.updatedTickers.emit(tickers)

    def stream(self):

        def fixed_supply_stream():
            feed = FixedSupplyCoinFeed().feed()
            while True:
                for coins in feed:
                    self.emit_coins(coins)

        def tickers_stream():
            tickersFeed = TickersFeed().feed()
            while True:
                for tickers in tickersFeed:
                    self.emit_tickers(tickers)

        thread = threading.Thread(target=fixed_supply_stream)
        thread.daemon = True
        thread.start()

        threadTickers = threading.Thread(target=tickers_stream)
        threadTickers.daemon = True
        threadTickers.start()