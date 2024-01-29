from robobopy_audiostream.RoboboAudio import RoboboAudio
from robobopy_audiostream.Exceptions import ClosedConnection
from robobopy.Robobo import Robobo
import pyaudio

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

server_address = 'YOUR_ROBOBO_IP_HERE'

rob = Robobo(server_address)
rob.connect()

rob.startAudioStream()

robAudio = RoboboAudio(server_address)
robAudio.connect()

while robAudio.isConnected():
    try:
        data = robAudio.getAudioWithMetadata()
        if (data != None):
            # Process audio data as needed
            timestamp, sync, audio_data = data
            print(f"Timestamp: {timestamp}, Sync: {sync}, Audio Data Length: {len(audio_data)}")
            stream.write(audio_data)
    except ClosedConnection:
        break
    except KeyboardInterrupt:
        break

robAudio.disconnect()

rob.stopAudioStream()
rob.disconnect()