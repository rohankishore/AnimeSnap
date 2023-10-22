import json
from PyQt6.QtWidgets import QFileDialog, QMessageBox


def json_to_tabular(self, include_all_details=False):
    # Accessing information in the JSON data
    result = self.a["result"]
    formatted_data = ""
    for entry in result:
        anilist = entry["anilist"]
        filename = entry["filename"]
        episode = entry["episode"]
        from_time = entry["from"]
        to_time = entry["to"]
        similarity = entry["similarity"] * 100
        video_url = entry["video"]
        image_url = entry["image"]

        # Format the data with labels and insert into the QTextEdit widget

        formatted_data += (
            f"Filename: {filename}\n"
            f"Episode: {episode}\n"
            f"From: {from_time}\n"
            f"To: {to_time}\n"
            f"Similarity: {similarity:.2f}%\n\n"
        )
        if include_all_details:
            formatted_data += (
                f"Anilist: {anilist}\n"
                f"Video URL: {video_url}\n"
                f"Image URL: {image_url}\n"
            )

    self.textbox.setPlainText(formatted_data)


def write_to_json(self):
    file_path, _ = QFileDialog.getSaveFileName(
        self,
        "Save JSON File",
        "",
        "JSON Files (*.json);;All Files (*)",
    )

    if file_path:
        try:
            # Open the selected file in write mode and write the JSON data
            with open(file_path, "w") as file:
                json.dump(self.a, file)

            # Inform the user that the file has been saved
            QMessageBox.information(
                self, "File Saved", "The file has been saved successfully."
            )
        except FileNotFoundError or PermissionError as e:
            # Handle any exceptions that may occur
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
