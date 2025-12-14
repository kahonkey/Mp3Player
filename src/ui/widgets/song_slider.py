from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt

class SongSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Orientation.Horizontal)
        self.setTracking(False)
        self.setObjectName("songSlider")
        self.setMaximum(100)
        self.setMinimum(0)
        self.setValue(0)