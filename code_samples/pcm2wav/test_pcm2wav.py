#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Package playsound
1. If package playsound is not installed, install it with pip3.

    $ sudo pip3 install playsound
    [sudo] password for aimldl: 
    Collecting playsound
      Downloading https://files.pythonhosted.org/packages/f5/16/10d897b0a83fb4b05b03a63d7a2667ab75f857f67f7062fd447dd3f49bf7/playsound-1.2.2-py2.py3-none-any.whl
    Installing collected packages: playsound
    Successfully installed playsound-1.2.2
    $

2. If playsound is installed on Python3, but ImportError occurs.
   
     $ python test_pcm2wav.py
     Traceback (most recent call last):
       File "test_pcm2wav.py", line 25, in <module>
         from playsound import playsound
     ImportError: No module named playsound

   Run it with the proper Python version that playsound is installed.
   Running with Python3 may fix the problem. Try python3, not python
   
     $ python3 test_pcm2wav.py    
-------------------------------------------------------------------------------
Last updated:  2019-06-11 (Tue)
First written: 2019-06-11 (Tue)
Written by Tae-Hyung "T" Kim, Ph.D.
  pcm2wav: Linux, Shell Scripting, Python을 써서 .pcm을 .wav로 파일 포맷 변환 (In Korean)
  https://aimldl.blog.me/221559323232
"""

# Difference between test_pcm2wav.py and pcm2wav.py
#  Only the following two lines are different.
#
# from playsound import playsound
# ...
# playsound( 'sample_001.wav' )

import wave
from playsound import playsound

# The parameters are prerequisite information. More specifically,
# channels, bit_depth, sampling_rate must be known to use this function.
def pcm2wav( pcm_file, wav_file, channels=1, bit_depth=16, sampling_rate=16000 ):

    # Check if the options are valid.
    if bit_depth % 8 != 0:
        raise ValueError("bit_depth "+str(bit_depth)+" must be a multiple of 8.")
        
    # Read the .pcm file as a binary file and store the data to pcm_data
    with open( pcm_file, 'rb') as opened_pcm_file:
        pcm_data = opened_pcm_file.read();
        
        obj2write = wave.open( wav_file, 'wb')
        obj2write.setnchannels( channels )
        obj2write.setsampwidth( bit_depth // 8 )
        obj2write.setframerate( sampling_rate )
        obj2write.writeframes( pcm_data )
        obj2write.close()

pcm2wav( 'sample_001.pcm', 'sample_001.wav', 1, 16, 16000 )
playsound( 'sample_001.wav' )

# Caution: do not enclose wave.open(...) with the 'with' keyword. That is,
#
#            with wave.open( wav_file, 'wb') as obj2write:
#              obj2write.setnchannels( channels )
#              ...
#
# will cause an error:
#
#   AttributeError: Wave_write instance has no attribute '__exit__'
#
# This error can be solved as the following suggestion.
#   [SOLVED] AttributeError: Wave_write instance has no attribute '__exit__'
#   https://tutel.me/c/programming/questions/46538867/attributeerror+wave_write+instance+has+no+attribute+39__exit__39
# But the code doens't look neat and more number of lines are required.
