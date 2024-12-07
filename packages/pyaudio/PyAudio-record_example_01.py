"""
PyAudio-Record_example_01.py

Example to show how to use record for PyAudio

Reference:
PyAudio, https://people.csail.mit.edu/hubert/pyaudio/
"""

import pyaudio
import wave
import sys
from os import path

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2

      

# Prepare the file
#filename = "jackhammer.wav"
filename = "harvard.wav"
dirname = "."
file = path.join(dirname, filename)

# Open the wave file "file" with rb (read, binary)
wf = wave.open( file, 'rb' )
sample_width = wf.getsampwidth()
channel = wf.getchannels()
framerate = wf.getframerate()

# Set up a PyAudio stream.
p = pyaudio.PyAudio()
stream = p.open( format =  p.get_format_from_width( sample_width ),
                 channels = channel,
                 rate = framerate,
                 output = True
                )

# Read frames (as much as the CHUNK size) from the wave file
# and write the read data to stream until no data is left.

data = wf.readframes( CHUNK )
while data !='':
    stream.write( data )
    data = wf.readframes( CHUNK )
    
stream.stop_stream()
stream.close()

p.terminate()
