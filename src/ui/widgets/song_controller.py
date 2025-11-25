from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from src.ui.widgets.pause_button import PauseButton
from src.engine.audio_engine import AudioEngine


class SongController(QFrame):
    def __init__(self):
        super().__init__()
        self.audio_eng = AudioEngine()
        self.is_paused = True
        self.setFixedSize(340, 540)
        self.setContentsMargins(25, 25, 25, 25)
        self.setObjectName("songController")
        self.song_image = QPixmap("placeholder.png").scaledToWidth(290, Qt.TransformationMode.SmoothTransformation)
        self.image = QLabel()
        self.image.setPixmap(self.song_image)
        self.image.setObjectName("songControlImage")
        self.song_title = QLabel("No song")
        self.song_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_title.setMinimumHeight(18)
        self.song_title.setObjectName("songName")
        self.album_name = QLabel("No song")
        self.album_name.setObjectName("albumName")
        self.album_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.album_name.setMinimumHeight(11)
        self.pause_button = PauseButton()
        self.pause_button.set_pause_icon(self.is_paused)
        self.pause_button.clicked.connect(self.pause_unpause)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.song_title)
        self.layout.addWidget(self.album_name)
        self.layout.addWidget(self.pause_button)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def set_song(self, title, artist, song_path):
        self.song_title.setText(f"{title} - {artist}")
        self.album_name.setText(song_path)
        self.audio_eng.load(song_path)
        self.audio_eng.play()
        self.is_paused = False

    def pause_unpause(self):
        if self.is_paused:
            self.audio_eng.unpause()
            self.is_paused = False
            self.pause_button.set_pause_icon(self.is_paused)
        else:
            self.audio_eng.pause()
            self.is_paused = True
            self.pause_button.set_pause_icon(self.is_paused)
