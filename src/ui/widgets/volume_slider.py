from PySide6.QtWidgets import QSlider, QFrame, QHBoxLayout
from PySide6.QtCore import Qt

class VolumeSlider(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setObjectName("volumeSlider")
        self.slider.setMaximum(100)
        self.slider.setMinimum(0)
        self.slider.setValue(50)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)