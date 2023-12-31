# robobo-python-audio-stream

This library is required to use the audio streaming from the Smartphone's microphone in the Robobo.py library. It only runs in Android operating system.

## Installation

Download this repository to your computer and save it in the *robobo.by* folder. Then open a terminal window and type the two following commands:

```
pip install robobopy_audiostream
```


## Example

The following script shows an example of the basic usage of this library:

``` python
from robobo_audio.robobo_audio import RoboboAudio
import pyaudio

SERVER_IP = "your_ip_here"

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
    except KeyboardInterrupt:
        break
        
audio.disconnect()
```