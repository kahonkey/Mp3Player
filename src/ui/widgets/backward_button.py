from PySide6.QtWidgets import QPushButton, QStyle
from PySide6.QtGui import QIcon, QPainter
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize


class BackwardButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(40, 40)
        self.setObjectName("controllerButton")
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSkipBackward)
        pixmap = icon.pixmap(QSize(38, 38))
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), Qt.GlobalColor.white)
        painter.end()
        self.setIcon(QIcon(pixmap))
        self.setIconSize(QSize(38,38))

