## Converting .pcm to .wav in Python

TODO: Usage doesn't work. Fix it.

https://pypi.org/project/PCM2Wav/
Project link, https://github.com/roel0/PCM2Wav-py

### Install the pcm2wav package
```bash
$ pip3 install pcm2wav
Collecting pcm2wav
  Downloading https://files.pythonhosted.org/packages/ca/10/d00ab0c7e52b617ab621f568c265c922997f80bcad6137e4a27293781375/PCM2Wav-1.2.tar.gz
Collecting wave (from pcm2wav)
  Downloading https://files.pythonhosted.org/packages/df/33/5a06e0c47a147b2683876ba7c576fad13e92b0b16755eb431e56c341e0cf/Wave-0.0.2.tar.gz
Building wheels for collected packages: pcm2wav, wave
  Running setup.py bdist_wheel for pcm2wav ... done
  Stored in directory: /home/aimldl/.cache/pip/wheels/76/7c/99/d72943b25f9bf66d784bf5baa134fc3edd026f3f4de8882797
  Running setup.py bdist_wheel for wave ... done
  Stored in directory: /home/aimldl/.cache/pip/wheels/8c/2e/ad/d96151afb1fdccf126346b26eabb91fec3c5ce5cbee7287fbf
Successfully built pcm2wav wave
Installing collected packages: wave, pcm2wav
Successfully installed pcm2wav-1.2 wave-0.0.2
$
```
### Usage
```bash
$ python
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from PCM2Wav import *
>>> output = PCM2Wav(PCM2Wav.saleae.I2S, "i2s.csv", "example.wav")
>>> exit()
$
```
