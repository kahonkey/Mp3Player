import sys

from PySide6.QtCore import QSize, Qt, QEvent
from PySide6.QtGui import QPalette
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
    QLineEdit
)


songs_list = {
    "Memento - nonoc.mp3": {
        "name": "Memento",
        "artist": "nonoc",
        "album": "rezero ending",
        "length": "5:04"
    },
    "STYX HELIX - MYTH & ROID.mp3": {
        "name": "STYX HELIX",
        "artist": "MYTH & ROID",
        "album": "rezero ending",
        "length": "4:50"
    },
    "Last Proof - ZAQ.mp3": {
        "name": "Last Proof",
        "artist": "ZAQ",
        "album": "ZAQ song",
        "length": "5:04"
    },
    "UP to ME - BiSH.mp3": {
        "name": "UP to ME",
        "artist": "BiSH",
        "album": "UP to ME",
        "length": "4:18"
    },
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)

        self.music_controller = QWidget()
        self.music_controller.setStyleSheet("background-color: #3B4D5E")
        self.playlist_viewer = PlaylistViewer()
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.music_controller)
        self.splitter.addWidget(self.playlist_viewer)
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


class PlaylistViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("playlistViewer")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
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
            song_button = SongButton(song["name"], song["artist"], song["album"], song["length"])
            song_button.setStyleSheet("width: 100%; height: 45px;")
            parent.addWidget(song_button)

    def count_songs(self, songs):
        return len(songs)

class TitleBar(QWidget):
    def __init__(self, count):
        super().__init__()
        self.setObjectName("titleBar")
        title_and_songs = QWidget()
        title_and_songs.layout = QVBoxLayout()
        title_and_songs.playlist_name = QLineEdit()
        title_and_songs.song_count = QLabel(f"{count} songs")
        title_and_songs.layout.addWidget(title_and_songs.playlist_name)
        title_and_songs.layout.addWidget(title_and_songs.song_count)
        title_and_songs.setLayout(title_and_songs.layout)
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.addWidget(title_and_songs)
        self.setLayout(self.layout)

class SongButton(QPushButton):
    def __init__(self, name, artist, album, length):
        super().__init__()

        self.layout = QHBoxLayout()

        self.name_label = QLabel(name)
        self.artist_label = QLabel(artist)
        self.album_label = QLabel(album)
        self.length_label = QLabel(length)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.artist_label)
        self.layout.addWidget(self.album_label)
        self.layout.addWidget(self.length_label)
        self.setStyleSheet(
            """
                QPushButton {
                    padding: 0px;
                    border: none;
                    background-color: #3B4D5E;
                }
            """)
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