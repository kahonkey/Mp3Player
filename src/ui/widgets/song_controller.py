from PySide6.QtWidgets import QFrame, QHBoxLayout
from src.ui.widgets.pause_button import PauseButton
from src.ui.widgets.forward_button import ForwardButton
from src.ui.widgets.backward_button import BackwardButton

class SongController(QFrame):
    def __init__(self):
        super().__init__()
        self.backward = BackwardButton()
        self.pause = PauseButton()
        self.forward = ForwardButton()
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.backward)
        self.layout.addWidget(self.pause)
        self.layout.addWidget(self.forward)
        self.setLayout(self.layout)
