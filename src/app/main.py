import sys
from collections.abc import Sequence

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QPixmap, QFont
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSplitter,
    QLineEdit,
    QFrame
)


songs_list = {
    "Memento - nonoc.mp3": {
        "name": "Memento",
        "artist": "nonoc",
        "file_path": "rezero ending",
        "length": "5:04"
    },
    "STYX HELIX - MYTH & ROID.mp3": {
        "name": "STYX HELIX",
        "artist": "MYTH & ROID",
        "file_path": "rezero ending",
        "length": "4:50"
    },
    "Last Proof - ZAQ.mp3": {
        "name": "Last Proof",
        "artist": "ZAQ",
        "file_path": "ZAQ song",
        "length": "5:04"
    },
    "UP to ME - BiSH.mp3": {
        "name": "UP to ME",
        "artist": "BiSH",
        "file_path": "UP to ME",
        "length": "4:18"
    },
}


class MainWindow(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.song_controller = SongController()
        self.music_controller = QFrame()
        self.music_controller.layout = QHBoxLayout()
        self.music_controller.layout.addWidget(self.song_controller)
        self.music_controller.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.music_controller.setLayout(self.music_controller.layout)
        self.playlist_viewer = PlaylistViewer(self.song_controller)
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.music_controller)
        self.splitter.addWidget(self.playlist_viewer)
        self.splitter.setSizes([500,300])
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)
        self.load_styles()

    def load_styles(self):
        try:
            with open('styles.qss', 'r') as f:
                style_sheet = f.read()
                self.setStyleSheet(style_sheet)
        except FileNotFoundError:
            print("Stylesheet not found, using default styles")

class SongController(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(340,540)
        self.setContentsMargins(25,25,25,25)
        self.setObjectName("songController")
        self.song_image = QPixmap("placeholder.png").scaledToWidth(290, Qt.TransformationMode.SmoothTransformation)
        self.image = QLabel()
        self.image.setPixmap(self.song_image)
        self.image.setObjectName("songControlImage")
        self.song_name = QLabel("No song")
        self.song_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_name.setMinimumHeight(18)
        self.song_name.setObjectName("songName")
        self.album_name = QLabel("No song")
        self.album_name.setObjectName("albumName")
        self.album_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.album_name.setMinimumHeight(11)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.song_name)
        self.layout.addWidget(self.album_name)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)
        
    def set_song(self, name, artist, song_path):
        self.song_name.setText(f"{name} - {artist}")
        self.album_name.setText(song_path)

class PlaylistViewer(QFrame):
    def __init__(self, song_controller: SongController):
        super().__init__()
        self.song_controller = song_controller
        self.setObjectName("playlistViewer")
        self.layout = QVBoxLayout()
        title_bar = TitleBar(self.count_songs(songs_list))
        self.layout.addWidget(title_bar)
        self.set_songs(songs_list, self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

    def set_songs(self, songs: dict, parent):
        for key in songs.keys():
            song = songs[key]
            index = list(songs.keys()).index(key)
            color = "#536C84" if index % 2 == 0 else "#3B4D5E"
            song_button = SongButton(song["name"], song["artist"], song["file_path"], song["length"])
            song_button.setStyleSheet(f"width: 100%; height: 45px; background-color: {color};")
            song_button.clicked.connect(lambda _, b=song_button:
                                        self.song_controller.set_song(b.name, b.artist, b.file_path)
                                        )
            parent.addWidget(song_button)

    def count_songs(self, songs):
        return len(songs)

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

class SongButton(QPushButton):
    def __init__(self, name, artist, file_path, length):
        super().__init__()
        self.setObjectName("songButton")

        self.layout = QHBoxLayout()
        
        self.name = name
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

# class CustomTitleBar(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.setAutoFillBackground(True)
#         self.setBackgroundRole(QPalette.ColorRole.Highlight)
#         self.initial_pos = None
#         title_bar_layout = QHBoxLayout(self)
#         title_bar_layout.setContentsMargins(0, 0, 0, 0)
#         title_bar_layout.setSpacing(0)
#         title_bar_layout.setVerticalSizeConstraint(QHBoxLayout.SizeConstraint.SetMaximumSize)
#
#         self.title = QLabel(f"{self.__class__.__name__}", self)
#         self.title.setStyleSheet("font-size: 9px")
#         self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         if title := parent.windowTitle():
#             self.title.setText(title)
#         title_bar_layout.addWidget(self.title)
#         # Min button
#         self.min_button = QToolButton(self)
#         min_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarMinButton
#         )
#         self.min_button.setIcon(min_icon)
#         self.min_button.clicked.connect(self.window().showMinimized)
#
#         # Max button
#         self.max_button = QToolButton(self)
#         max_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarMaxButton
#         )
#         self.max_button.setIcon(max_icon)
#         self.max_button.clicked.connect(self.window().showMaximized)
#
#         # Close button
#         self.close_button = QToolButton(self)
#         close_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarCloseButton
#         )
#         self.close_button.setIcon(close_icon)
#         self.close_button.clicked.connect(self.window().close)
#
#         # Normal button
#         self.normal_button = QToolButton(self)
#         normal_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarNormalButton
#         )
#         self.normal_button.setIcon(normal_icon)
#         self.normal_button.clicked.connect(self.window().showNormal)
#         self.normal_button.setVisible(False)
#         # Add buttons
#         buttons = [
#             self.min_button,
#             self.normal_button,
#             self.max_button,
#             self.close_button,
#         ]
#         for button in buttons:
#             button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#             button.setFixedSize(QSize(11, 11))
#             #button.setStyleSheet()
#             title_bar_layout.addWidget(button)
#
#     def window_state_changed(self, state):
#         if state == Qt.WindowState.WindowMaximized:
#             self.normal_button.setVisible(True)
#             self.max_button.setVisible(False)
#         else:
#             self.normal_button.setVisible(False)
#             self.max_button.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    widget.resize(785, 600)
    widget.show()

    sys.exit(app.exec())


# if __name__ == "__main__":
#     from .application import MP3PlayerApplication
#     app = MP3PlayerApplication()
#     app.run()