from tkinter import END, filedialog, messagebox
import os.path

import requests
import json
from customtkinter import *

def search(self):
    self.geometry("750x800")
    self.a = requests.post("https://api.trace.moe/search",
                           files={"image": open(f"{self.img_path}", "rb")}
                           ).json()
    print(self.a)


    self.textbox = CTkTextbox(self)
    self.textbox.pack(pady=10, fill=Y)

    CTkButton(self, text="Write to JSON (includes much more details)", command=lambda : json_operations.write_to_json(self), cursor="hand2").pack(side=BOTTOM, pady=15)
    CTkButton(self, text="Search Another Image", command=self.returnToMenu, cursor="hand2").pack(side=BOTTOM)