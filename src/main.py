from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import *

import AnimeSearch


class Window(MSFluentWindow):
    """ Main window class. Uses MSFLuentWindow to imitate the Windows 11 FLuent Design windows. """

    def __init__(self):
        # self.isMicaEnabled = False
        super().__init__()
        #self.setTitleBar(CustomTitleBar(self))
        #self.tabBar = self.titleBar.tabBar  # type: TabBar

        setTheme(Theme.DARK)


        # create sub interface
        self.homeInterface = AnimeSearch.App()
        # self.settingInterface = Settings()
        # self.settingInterface.setObjectName("markdownInterface")


        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.SEARCH, "Find Anime", FIF.SEARCH, NavigationItemPosition.TOP)
        # self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', FIF.SETTING,  NavigationItemPosition.BOTTOM)
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.INFO,
            text='About',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM)

        self.navigationInterface.setCurrentItem(
            self.homeInterface.objectName())

    def initWindow(self):
        self.resize(500, 160)
        self.setWindowIcon(QIcon('resource/icon.ico'))
        self.setWindowTitle('ZenNotes')

        w, h = 1200, 800
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def showMessageBox(self):
        w = MessageBox(
            'AnimeSnap 🏯',
            (
                    "Version : 3.0"
                    + "\n" + "\n" + "\n" + "💝  I hope you'll enjoy using AnimeSnap as much as I did while coding it  💝" + "\n" + "\n" + "\n" +
                    "Made with 💖 By Rohan Kishore"
            ),
            self
        )
        w.yesButton.setText('GitHub')
        w.cancelButton.setText('Return')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/rohankishore/"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    #qdarktheme.setup_theme("dark")
    window = Window()
    window.show()
    sys.exit(app.exec())
