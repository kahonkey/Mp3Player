from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from src.ui.widgets.song_controller import SongController
from src.engine.audio_engine import AudioEngine


class SongInfo(QFrame):
    def __init__(self, songs_list):
        super().__init__()
        self.songs_list = songs_list
        self.current_index = 0
        self.audio_eng = AudioEngine()
        self.is_paused = True
        self.setFixedSize(339, 540)
        self.setContentsMargins(24, 25, 25, 25)
        self.setObjectName("songInfo")
        self.song_image = QPixmap("placeholder.png").scaledToWidth(290, Qt.TransformationMode.SmoothTransformation)
        self.image = QLabel()
        self.image.setPixmap(self.song_image)
        self.image.setObjectName("songInfosImage")
        self.song_title = QLabel("No song")
        self.song_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_title.setMinimumHeight(18)
        self.song_title.setObjectName("songName")
        self.album_name = QLabel("No song")
        self.album_name.setObjectName("albumName")
        self.album_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.album_name.setMinimumHeight(11)
        self.song_controller = SongController()
        self.song_controller.pause.set_pause_icon(self.is_paused)
        self.song_controller.pause.clicked.connect(self.pause_unpause)
        self.song_controller.forward.clicked.connect(self.play_next)
        self.song_controller.backward.clicked.connect(self.play_previous)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.song_title)
        self.layout.addWidget(self.album_name)
        self.layout.addWidget(self.song_controller)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def set_song(self, title, artist, song_path, album_cover):
        self.song_title.setText(f"{title} - {artist}")
        self.album_name.setText(song_path)
        self.audio_eng.load(song_path)
        if album_cover is None:
            self.song_image = QPixmap("placeholder.png").scaledToWidth(290, Qt.TransformationMode.SmoothTransformation)
        else:
            self.song_image.loadFromData(album_cover)
            self.song_image = self.song_image.scaledToWidth(290, Qt.TransformationMode.SmoothTransformation)
        self.image.setPixmap(self.song_image)
        self.audio_eng.play()
        self.is_paused = False
        self.song_controller.pause.set_pause_icon(self.is_paused)

    def pause_unpause(self):
        if self.is_paused:
            self.audio_eng.unpause()
            self.is_paused = False
            self.song_controller.pause.set_pause_icon(self.is_paused)
        else:
            self.audio_eng.pause()
            self.is_paused = True
            self.song_controller.pause.set_pause_icon(self.is_paused)

    def play_next(self):
        if not self.songs_list:
            return

        self.current_index = (self.current_index + 1) % len(self.songs_list)
        song = self.songs_list[self.current_index]
        self.set_song(song.title, song.artist, song.file_path, song.album_cover)


    def play_previous(self):
        if not self.songs_list:
            return

        self.current_index = (self.current_index - 1) % len(self.songs_list)
        song = self.songs_list[self.current_index]
        self.set_song(song.title, song.artist, song.file_path, song.album_cover)

