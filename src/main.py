import os.path
import json_operations
import search
import requests
import json
from customtkinter import *
from tkinter import END, filedialog, messagebox



class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("AnimeSearch")
        self.geometry("450x150")

        self.img_path = ""

        self.buttons_frame = CTkFrame(self, height=300)
        self.buttons_frame.pack(fill=X)

        CTkButton(self.buttons_frame, text="Open Image", cursor="hand2", command=self.open_image).pack(pady=15)
        self.file_path_label = CTkLabel(self.buttons_frame, text="")
        self.file_path_label.pack()

        CTkButton(self, text="Search", cursor="hand2", command=self.onClickSearch).pack(pady=15, side=BOTTOM)


    def open_image(self):
        a = filedialog.askopenfilename(title="Open Image to Search")
        a = str(os.path.abspath(a))
        self.img_path = a
        self.file_path_label.configure(text=a)


    def returnToMenu(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.geometry("450x150")
        self.buttons_frame = CTkFrame(self, height=300)
        self.buttons_frame.pack(fill=X)

        CTkButton(self.buttons_frame, text="Open Image", cursor="hand2", command=self.open_image).pack(pady=15)
        self.file_path_label = CTkLabel(self.buttons_frame, text="")
        self.file_path_label.pack()

        CTkButton(self, text="Search", cursor="hand2", command=self.onClickSearch).pack(pady=15, side=BOTTOM)


    def onClickSearch(self):
        for widget in self.winfo_children():
            widget.destroy()

        search.search(self)
        json_operations.json_to_tabular(self)



if "__main__" == __name__:
    app = App()
    app.mainloop()
