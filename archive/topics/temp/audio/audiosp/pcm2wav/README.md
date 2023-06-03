README.md

Last updated: 2019-07-01 (Mon)
@author: aimldl

# Test pcm2wav with src/main.py
## src/main.py
  is an example Python script that converts 
  .pcm files in directory 'pcm' to .wav files in directory 'wav'.
 
## src/audiosp.py
  audiosp module has class AudioSignalProcessing where pcm2wav is a member function.

This script is designed to run by run_pcm2wav
  $ ./run_pcm2wav
because it's assumed os.curdir is where run_pcm2wav is located.

# Directory & File Structure
$ tree audiosp-pcm2wav/
audiosp-pcm2wav/
├── README.md
├── pcm
│   ├── wake_word-amazon-alexa.pcm
│   ├── wake_word-amazon-amazon.pcm
│   ├── wake_word-amazon-computer.pcm
│   └── wake_word-amazon-echo.pcm
├── run_pcm2wav
├── src
│   ├── __pycache__
│   │   └── audiosp.cpython-36.pyc
│   ├── audiosp.py
│   └── main.py
└── wav
    ├── wake_word-amazon-alexa.wav
    ├── wake_word-amazon-amazon.wav
    ├── wake_word-amazon-computer.wav
    └── wake_word-amazon-echo.wav

4 directories, 13 files
$
