import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar=QToolBar()
        self.addToolBar(navbar)

        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        fordward_btn = QAction('Forward', self)
        back_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fordward_btn)

        reload_btn = QAction('Reload', self)
        back_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        back_btn.triggered.connect(self.nevigation_home)
        navbar.addAction(home_btn)

        self.Url_bar=QLineEdit()
        self.Url_bar.returnPressed.connect(self.nevigate_to_url)
        navbar.addWidget(self.Url_bar)

        #self.browser.urlChanged.connect(self.update_url)

    def nevigation_home(self):

        self.browser.setUrl(QUrl("https://google.com"))

    def nevigate_to_url(self):

        url = self.Url_bar.text()
        self.browser.setUrl(QUrl('url'))


app=QApplication(sys.argv)
QApplication.setApplicationName("This is Ganesh Browser ")


window=MainWindow()
app.exec()
