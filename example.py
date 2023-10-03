from robobopy_audiostream.RoboboAudio import RoboboAudio
from robobopy.Robobo import Robobo
import pyaudio

SERVER_IP = "192.168.1.238"

p = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

audio = RoboboAudio(SERVER_IP)
audio.connect()

audio.syncAudioQueue()
while True:
    try:
        audioData = audio.getAudioWithMetadata()
        if not audioData is None:
            data, ts, snc = audioData
            stream.write(data)
        else:
            break
    except KeyboardInterrupt:
        break
        
audio.disconnect()