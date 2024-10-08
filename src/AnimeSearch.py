import sys
import os
import json_operations
import search
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import *

import qdarktheme
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("AnimeSnap")
        self.setGeometry(100, 100, 450, 150)

        self.mainApp = parent

        # Create a stacked widget to manage different screens
        self.stacked_widget = QStackedWidget(self)

        # Create the main menu widget
        self.main_menu_widget = QWidget(self)
        self.stacked_widget.addWidget(self.main_menu_widget)

        self.img_path = ""
        self.img_url = ""
        self.anilist_id = ""
        self.ctheme = "dark"

        layout = QVBoxLayout(self)
        layout.addStretch()
        self.setLayout(layout)

        self.buttons_frame = QWidget(self)
        layout.addWidget(self.buttons_frame)

        # Create a horizontal layout
        top_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        checkbox_layout = QHBoxLayout()

        layout.addLayout(top_layout)

        layout.addWidget(QLabel(""))

        self.img_url_entry = LineEdit(self)
        self.img_url_entry.setPlaceholderText("Enter image URL or Upload an image")

        self.file_path_label = CaptionLabel()

        button_layout.addWidget(self.img_url_entry)

        open_image_icon = QIcon("icons/folder.png")
        self.open_image_button = QPushButton(self)
        self.open_image_button.setStyleSheet("""
        QPushButton {
        border: none;
        }
        """)
        self.open_image_button.clicked.connect(self.open_image)
        self.open_image_button.setIcon(open_image_icon)
        self.open_image_button.setIconSize(QSize(23, 23))
        self.open_image_button.setFixedSize(28, 28)
        button_layout.addWidget(self.open_image_button)

        layout.addLayout(button_layout)  # Add the button layout to the main layout
        layout.addWidget(self.file_path_label)

        layout.addWidget(QLabel(""))

        layout.addLayout(checkbox_layout)  # Add the checkbox layout to the main layout

        self.checkbox_rbb = CheckBox()
        self.checkbox_rbb.setText("Remove Black Borders")
        checkbox_layout.addWidget(self.checkbox_rbb)

        self.checkbox_iad = CheckBox()
        self.checkbox_iad.setText("Include All Details")
        checkbox_layout.addWidget(self.checkbox_iad)

        layout.addWidget(QLabel(""))

        anilist_label = CaptionLabel()
        anilist_label.setText("Anilist Anime ID [OPTIONAL] [https://anilist.co/]")
        layout.addWidget(anilist_label)

        self.anilist_entry = LineEdit(self)
        self.anilist_entry.setPlaceholderText(
            "Use this if you know what anime it is and you just need the scene details"
        )
        layout.addWidget(self.anilist_entry)

        search_button = PrimaryPushButton()
        search_button.setText("Search")
        search_button.clicked.connect(self.onClickSearch)
        layout.addWidget(search_button)

    def open_image(self):
        # options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image to Search",
            "",
            "Image Files (*.jpg *.png *.bmp);;All Files (*)",
        )

        if file_path:
            self.img_path = file_path
            self.file_path_label.setText(file_path)

    def returnToMenu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)
        self.img_path = ""
        self.file_path_label.setText("")  # Use self.file_path_label instead of self.main_menu_widget.file_path_label

    def onClickSearch(self):
        self.img_url = self.img_url_entry.text()
        anilist_id = self.anilist_entry.text()
        iad_status = self.checkbox_iad.isChecked()
        rbb_status = self.checkbox_rbb.isChecked()
        anilist_status = anilist_id if anilist_id else None

        if self.img_url or self.img_path != "":
            while self.layout().count():
                item = self.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

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
                json_operations.json_to_tabular(self, include_all_details=True)
            else:
                json_operations.json_to_tabular(self, include_all_details=False)

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error")
            dlg.setText("Select any Image or Enter any URL to search")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                pass
            else:
                pass
