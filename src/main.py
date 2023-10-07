import sys
import os
import json_operations
import search
import qdarktheme
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AnimeSnap")
        self.setGeometry(100, 100, 450, 150)

        self.img_path = ""
        self.img_url = ""
        self.anilist_id = ""
        self.ctheme = "dark"

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.buttons_frame = QWidget()
        layout.addWidget(self.buttons_frame)

        # Create a horizontal layout
        top_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        checkbox_layout = QHBoxLayout()

        theme_icon = QIcon("icons/dark.png")
        self.themes_button = QPushButton(self)
        self.themes_button.setIconSize(QSize(23, 23))
        self.themes_button.clicked.connect(self.onClickThemeIcon)
        self.themes_button.setIcon(theme_icon)
        self.themes_button.setText("")
        self.themes_button.setFixedSize(23, 23)
        top_layout.addStretch()
        top_layout.addWidget(self.themes_button)

        layout.addLayout(top_layout)

        layout.addWidget(QLabel(""))

        self.img_url_entry = QLineEdit(self)
        self.img_url_entry.setPlaceholderText("Enter image URL or Upload a image")

        self.file_path_label = QLabel("")

        button_layout.addWidget(self.img_url_entry)


        open_image_icon = QIcon("icons/folder.png")
        self.open_image_button = QPushButton(self)
        self.open_image_button.clicked.connect(self.open_image)
        self.open_image_button.setIcon(open_image_icon)
        self.open_image_button.setIconSize(QSize(23, 23))
        self.open_image_button.setFixedSize(28, 28)
        button_layout.addWidget(self.open_image_button)

        layout.addLayout(button_layout)# Add the button layout to the main layout
        layout.addWidget(self.file_path_label)

        layout.addWidget(QLabel(""))

        layout.addLayout(checkbox_layout)  # Add the checkbox layout to the main layout

        self.checkbox_rbb = QCheckBox("Remove Black Borders")
        checkbox_layout.addWidget(self.checkbox_rbb)

        self.checkbox_iad = QCheckBox("Include All Details")
        checkbox_layout.addWidget(self.checkbox_iad)

        layout.addWidget(QLabel(""))

        layout.addWidget(QLabel("Anilist Anime ID [OPTIONAL] [https://anilist.co/]"))

        self.anilist_entry = QLineEdit(self)
        self.anilist_entry.setPlaceholderText("Use this if you know what anime it is and you just need the scene details")
        layout.addWidget(self.anilist_entry)


        search_button = QPushButton("Search")
        search_button.clicked.connect(self.onClickSearch)
        layout.addWidget(search_button)

    def open_image(self):
        #options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image to Search", "", "Image Files (*.jpg *.png *.bmp);;All Files (*)")

        if file_path:
            self.img_path = file_path
            self.file_path_label.setText(file_path)

    def returnToMenu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)
        self.img_path = ""
        self.main_menu_widget.file_path_label.setPlainText("")

    def onClickThemeIcon(self):
        if self.ctheme == "dark":
            self.ctheme = "light"
            qdarktheme.setup_theme("light")
        else:
            self.ctheme = "dark"
            qdarktheme.setup_theme("dark")
        self.onThemeIconVisibilityChanged()

    def onThemeIconVisibilityChanged(self):
        if self.ctheme == "dark":
            self.themes_button.setIcon(QIcon('icons/dark.png'))
        else:
            self.themes_button.setIcon(QIcon('icons/light.png'))

    def onClickSearch(self):
        # Clear the layout
        while self.layout().count():
            item = self.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.img_url = self.img_url_entry.text()
        anilist_id = self.anilist_entry.text()
        anilist_status = ""
        rbb_status = ""
        iad_status = ""

        if self.checkbox_iad.isChecked():
            iad_status = True
        else:
            iad_status = False

        if self.checkbox_rbb.isChecked():
            rbb_status = True
        else:
            rbb_status = False

        if anilist_id == "":
            anilist_status = None
        else:
            anilist_status = anilist_id

        if self.img_url == "":
            search.search_img(self, anilist_info=anilist_status, rbb=rbb_status)
        else:
            search.search_url(self)

        if iad_status is True:
            json_operations.json_to_tabular(self, iad=True)
        else:
            json_operations.json_to_tabular(self, iad=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark")
    window = App()
    window.show()
    sys.exit(app.exec())
