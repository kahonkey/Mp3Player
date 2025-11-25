import pygame
from pygame import mixer
from pathlib import Path


class AudioEngine:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.current_file = None
        self.is_paused = False

    def load(self, file_path: str):
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if file_path.suffix.lower() not in [".mp3", ".wav", ".ogg"]:
            raise ValueError("Unsupported audio format")

        self.current_file = str(file_path)
        mixer.music.load(self.current_file)

    def play(self):
        if not self.current_file:
            raise RuntimeError("No audio file loaded")

        mixer.music.play()
        self.is_paused = False

    def stop(self):
        mixer.music.stop()
        self.is_paused = False

    def pause(self):
        if not self.is_paused:
            mixer.music.pause()
            self.is_paused = True

    def unpause(self):
        if self.is_paused:
            mixer.music.unpause()
            self.is_paused = False

    def set_volume(self, volume: float):
        volume = max(0.0, min(1.0, volume))
        mixer.music.set_volume(volume)

    def get_volume(self) -> float:
        return mixer.music.get_volume()

    def is_playing(self) -> bool:
        return mixer.music.get_busy()
