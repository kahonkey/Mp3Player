from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from src.ui.widgets.song_controller import SongController
from src.engine.audio_engine import AudioEngine


class SongInfo(QFrame):
    def __init__(self, audio_eng: AudioEngine):
        super().__init__()
        self.ignore_updates = False
        self.audio_eng = audio_eng
        self.is_paused = True
        self.current_position = 0
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
        self.song_controller.volume.slider.valueChanged.connect(lambda v: self.set_volume(float(v)/100))
        self.song_controller.song_slider.sliderPressed.connect(self.on_slider_pressed)
        self.song_controller.song_slider.sliderReleased.connect(self.on_slider_released)
        self.song_controller.song_slider.sliderMoved.connect(self.set_position)
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.set_position_slider)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.song_title)
        self.layout.addWidget(self.album_name)
        self.layout.addWidget(self.song_controller)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def set_song(self, title, artist, song_path, album_cover, length):
        self.timer.start()
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
        self.song_controller.song_slider.setMaximum(length)
        minutes = str(int(length / 60))
        seconds = str(int(length % 60))
        seconds = "0" + seconds if len(seconds) < 2 else seconds
        self.song_controller.song_length_label.setText(f"{minutes}:{seconds}")
        self.current_position = 0

    def pause_unpause(self):
        if self.is_paused:
            self.timer.start()
            self.audio_eng.unpause()
            self.is_paused = False
            self.song_controller.pause.set_pause_icon(self.is_paused)
        else:
            self.timer.stop()
            self.audio_eng.pause()
            self.is_paused = True
            self.song_controller.pause.set_pause_icon(self.is_paused)

    def set_volume(self, volume):
        self.audio_eng.set_volume(volume)

    def on_slider_pressed(self):
        self.ignore_updates = True

    def on_slider_released(self):
        self.ignore_updates = False
        self.audio_eng.set_position(self.current_position)

    def set_position(self, pos):
        self.current_position = pos

    def set_position_slider(self):
        if not self.ignore_updates:
            self.current_position = self.audio_eng.get_position()
            print(self.audio_eng.get_position())
            self.song_controller.song_slider.setValue(self.current_position)
        minutes = str(int(self.current_position / 60))
        seconds = str(int(self.current_position % 60))
        seconds = "0" + seconds if len(seconds) < 2 else seconds
        self.song_controller.song_pos_label.setText(f"{minutes}:{seconds}")