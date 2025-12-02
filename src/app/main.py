import sys
import os
import pickle
from mutagen.mp3 import MP3
import glob
from src.engine.audio_engine import AudioEngine
from song import Song

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QSplitter,
    QFrame
)

from src.ui.widgets.song_info import SongInfo
from src.ui.widgets.playlist_viewer import PlaylistViewer

audio_eng = AudioEngine()

songs_list = []

if not glob.glob("playlist"):
    os.mkdir("playlist")


class MainWindow(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.song_controller = SongInfo()
        self.music_controller = QFrame()
        self.music_controller.layout = QHBoxLayout()
        self.music_controller.layout.addWidget(self.song_controller)
        self.music_controller.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.music_controller.setLayout(self.music_controller.layout)
        self.playlist_viewer = PlaylistViewer(self.song_controller, songs_list)
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


def init_songs():
    if len(glob.glob("songs/*.mp3")) > len(glob.glob("playlist/*.pkl")):
        for song in glob.glob("songs/*.mp3"):
            audio = MP3(song)
            new_song = Song(str(audio.get("TIT2")), str(audio.get("TPE1")), song, audio.info.length, get_album_cover(audio))
            songs_list.append(new_song)
        for song in songs_list:
            with open(f"playlist/{song.title}-{song.artist}.pkl", "wb") as f:
                pickle.dump(song, f)
        return
    
    for song in glob.glob("playlist/*.pkl"):
        with open(song, "rb") as f:
            unpickled_song = pickle.load(f)
        songs_list.append(unpickled_song)
        
def get_album_cover(audio):
    # Check for APIC frame (album art)
    if 'APIC:' in audio.tags:
        artwork = audio.tags['APIC:'].data
        print(artwork)
        return artwork
    else:
        print("asdwad")
        return None

if __name__ == "__main__":
    init_songs()
    app = QApplication(sys.argv)
    widget = MainWindow()
    
    widget.resize(785, 600)
    widget.show()

    sys.exit(app.exec())