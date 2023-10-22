import urllib

import requests
from PyQt6.QtWidgets import QVBoxLayout, QTextEdit, QPushButton, QWidget

import json_operations


def search_img(self, anilist_info=None, rbb=False):
    self.setGeometry(100, 100, 750, 800)
    self.a = ""

    if anilist_info is None:
        self.a = requests.post(
            "https://api.trace.moe/search",
            files={"image": open(f"{self.img_path}", "rb")},
        ).json()
    else:
        if rbb is False:
            url = f"https://api.trace.moe/search?anilistID={anilist_info}&url=" + "{}"
            self.a = requests.get(
                url.format(urllib.parse.quote_plus(f"{self.img_path}"))
            ).json()
        else:
            url = f"https://api.trace.moe/search?anilistID={anilist_info}&url=" + "{}"
            self.a = requests.get(
                url.format(urllib.parse.quote_plus(f"{self.img_path}"))
            ).json()

    self.textbox = QTextEdit()
    self.textbox.setPlainText(str(self.a) + "\n" + "\n")
    self.textbox.setReadOnly(True)

    layout = QVBoxLayout()
    layout.addWidget(self.textbox)

    json_button = QPushButton("Write to JSON")
    json_button.clicked.connect(lambda: json_operations.write_to_json(self))
    layout.addWidget(json_button)

    another_image_button = QPushButton("Search Another Image")
    another_image_button.clicked.connect(self.returnToMenu)
    layout.addWidget(another_image_button)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    self.setCentralWidget(central_widget)


def search_url(self, anilist_info=None, rbb=False):
    self.setGeometry(100, 100, 750, 800)
    self.a = ""
    if anilist_info is None:
        self.a = requests.post(
            "https://api.trace.moe/search",
            files={"image": open(f"{self.img_url}", "rb")},
        ).json()
    else:
        if rbb is False:
            url = f"https://api.trace.moe/search?anilistID={anilist_info}&url=" + "{}"
            self.a = requests.get(
                url.format(urllib.parse.quote_plus(f"{self.img_url}"))
            ).json()
        else:
            url = (
                "https://api.trace.moe/search?anilistID"
                + str(anilist_info)
                + "&url="
                + "{}"
            )
            self.a = requests.get(
                url.format(urllib.parse.quote_plus(f"{self.img_url}"))
            ).json()

    self.textbox = QTextEdit()
    self.textbox.setPlainText(str(self.a) + "\n" + "\n")
    self.textbox.setReadOnly(True)

    layout = QVBoxLayout()
    layout.addWidget(self.textbox)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    self.setCentralWidget(central_widget)
