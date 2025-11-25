from PySide6.QtWidgets import QFrame, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout

class TitleBar(QFrame):
    def __init__(self, count):
        super().__init__()
        self.setObjectName("titleBar")
        title_and_songs = QFrame()
        title_and_songs.setObjectName("titleAndSongs")
        title_and_songs.layout = QVBoxLayout()
        title_and_songs.playlist_name = QLineEdit()
        title_and_songs.song_count = QLabel(f"{count} songs")
        title_and_songs.layout.addWidget(title_and_songs.playlist_name)
        title_and_songs.layout.addWidget(title_and_songs.song_count)
        title_and_songs.setLayout(title_and_songs.layout)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(title_and_songs)
        self.setFixedHeight(45)
        self.setLayout(self.layout)
