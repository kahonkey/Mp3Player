from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QObject
import os

class FileDialog(QObject):

    @staticmethod
    def open_mp3_files(parent=None):
        files, _ = QFileDialog.getOpenFileNames(
            parent,
            caption="Select MP3 Files",
            filter="Audio Files (*.mp3)"
        )

        return [f for f in files if os.path.exists(f)]
