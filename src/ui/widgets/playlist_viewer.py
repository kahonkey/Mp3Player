from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import Qt
from src.ui.widgets.title_bar import TitleBar
from src.ui.widgets.song_button import SongButton


class PlaylistViewer(QFrame):
    def __init__(self, song_controller, songs_list):
        super().__init__()
        self.songs_list = songs_list
        self.song_controller = song_controller
        self.setObjectName("playlistViewer")
        self.layout = QVBoxLayout()
        title_bar = TitleBar(self.count_songs(self.songs_list))
        self.layout.addWidget(title_bar)
        self.set_songs(self.songs_list, self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

    def set_songs(self, songs: list, parent):
        for song in songs:
            index = songs.index(song)
            color = "#536C84" if index % 2 == 0 else "#3B4D5E"
            song_button = SongButton(song.title, song.artist, song.file_path, song.length)
            song_button.setStyleSheet(f"width: 100%; height: 45px; background-color: {color};")
            song_button.clicked.connect(lambda _, b=song_button:
                                        self.song_controller.set_song(b.title, b.artist, b.file_path)
                                        )
            parent.addWidget(song_button)

    def count_songs(self, songs):
        return len(songs)
