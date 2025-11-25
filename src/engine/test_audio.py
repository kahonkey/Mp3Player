from audio_engine import AudioEngine
import time

player = AudioEngine()

player.load("Pitbull_feat._G.R.L._—_Wild_Wild_Love_.mp3")
player.play()

time.sleep(3)
player.pause()

time.sleep(2)
player.unpause()

time.sleep(5)
player.stop()
