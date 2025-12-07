from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel
from src.ui.widgets.pause_button import PauseButton
from src.ui.widgets.forward_button import ForwardButton
from src.ui.widgets.backward_button import BackwardButton
from src.ui.widgets.volume_slider import VolumeSlider
from src.ui.widgets.song_slider import SongSlider
from src.engine.audio_engine import AudioEngine

class SongController(QFrame):
    def __init__(self):
        super().__init__()
        self.backward = BackwardButton()
        self.pause = PauseButton()
        self.forward = ForwardButton()
        self.volume = VolumeSlider()
        self.song_slider = SongSlider()
        self.song_pos_label = QLabel("--:--")
        self.song_length_label = QLabel("--:--")
        self.layout = QVBoxLayout()
        self.controls = QHBoxLayout()
        self.song_pos = QHBoxLayout()
        self.controls.addWidget(self.backward)
        self.controls.addWidget(self.pause)
        self.controls.addWidget(self.forward)
        self.song_pos.addWidget(self.song_pos_label)
        self.song_pos.addWidget(self.song_slider)
        self.song_pos.addWidget(self.song_length_label)
        self.layout.addLayout(self.controls)
        self.layout.addLayout(self.song_pos)
        self.layout.addWidget(self.volume)
        self.setFixedHeight(150)
        self.setLayout(self.layout)


