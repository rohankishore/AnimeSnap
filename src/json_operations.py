from tkinter import END, filedialog, messagebox
import os.path

import requests
import json
from customtkinter import *

def json_to_tabular(self):
        # Accessing information in the JSON data
        result = self.a['result']

        for entry in result:
            filename = entry['filename']
            episode = entry['episode']
            from_time = entry['from']
            to_time = entry['to']
            similarity = entry['similarity'] * 100 , "%"
            video_url = entry['video']
            image_url = entry['image']

            # Format the data with labels and insert into the Text widget
            formatted_data = (
                f"Filename: {filename}\n"
                f"Episode: {episode}\n"
                f"From: {from_time}\n"
                f"To: {to_time}\n"
                f"Similarity: {similarity}\n"
                #f"Video URL: {video_url}\n"
                #f"Image URL: {image_url}\n\n"
            )
            self.textbox.insert(END, (formatted_data + "\n" + "\n" + "\n"))

            # Disable text editing
        self.textbox.configure(state=DISABLED, width=700, height=650)

def write_to_json(self):
        # Open a file dialog to select a file to write to
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("JSON Files", "*.json")])

        if file_path:
            try:
                # Open the selected file in write mode and write the text
                with open(file_path, "w") as file:
                    self.a = json.dumps(self.a)
                    file.write(self.a)

                # Inform the user that the file has been saved
                messagebox.showinfo("File Saved", "The file has been saved successfully.")
            except Exception as e:
                # Handle any exceptions that may occur
                messagebox.showerror("Error", f"An error occurred: {str(e)}")