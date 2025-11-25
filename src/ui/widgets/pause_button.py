from PySide6.QtWidgets import QPushButton, QStyle

class PauseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setObjectName("pauseButton")

    def set_pause_icon(self, is_paused):
        if is_paused:
            icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        else:
            icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
        self.setIcon(icon)
