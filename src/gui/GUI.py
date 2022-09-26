
import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from coins.gui.misc.Clock import Clock
from coins.gui.feeds.MainCoinFeed import MainCoinFeed

class GuiRunner():
    '''Runs the qt application'''

    def __init__(self):
        '''Instantiates the qt application'''
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.quit.connect(self.app.quit)

    def run(self):
        '''Loads images and starts all data threads'''
        self.engine.load('coins/gui/main.qml')
        self.startClock()
        self.startCoinFeeds()

  
    def startClock(self):
        '''Thread providing a time feed to the gui'''
        clock = Clock()
        print('-------------', self.engine.rootObjects())
        self.engine.rootObjects()[0].setProperty('clock', clock)
        clock.start()

    def startCoinFeeds(self):
        '''Creates theads providing coin data to the gui'''
        coin_stream = MainCoinFeed()
        self.engine.rootObjects()[0].setProperty('coinStream', coin_stream)
        coin_stream.stream()

        sys.exit(self.app.exec())