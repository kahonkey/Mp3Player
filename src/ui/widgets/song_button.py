from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel

class SongButton(QPushButton):
    def __init__(self, name, artist, file_path, length):
        super().__init__()
        self.setObjectName("songButton")

        self.layout = QHBoxLayout()

        self.title = name
        self.artist = artist
        self.file_path = file_path

        self.name_label = QLabel(name)
        self.artist_label = QLabel(artist)
        self.file_path_label = QLabel(file_path)
        self.length_label = QLabel(length)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.artist_label)
        self.layout.addWidget(self.file_path_label)
        self.layout.addWidget(self.length_label)
        self.setLayout(self.layout)
