
import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from src.gui.misc.Clock import Clock
from src.gui.feeds.Feeds import Feeds

class GuiRunner():
    '''Runs the qt application'''

    def __init__(self):
        '''Instantiates the qt application'''
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.quit.connect(self.app.quit)

    def run(self):
        '''Loads images and starts all data threads'''

        def startClock():
            '''Thread providing a time feed to the gui'''
            clock = Clock()
            self.engine.rootObjects()[0].setProperty('clock', clock)
            clock.start()

        def startCoinFeeds():
            '''Creates theads providing coin data to the gui'''
            coin_stream = Feeds()
            self.engine.rootObjects()[0].setProperty('coinStream', coin_stream)
            coin_stream.stream()

        self.engine.load('src/gui/main.qml')
        startClock()
        startCoinFeeds()

        sys.exit(self.app.exec())