#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audio signal processing, https://en.wikipedia.org/wiki/Audio_signal_processing

Last updated:  2019-06-27 (Thu)
First written: 2019-06-11 (Tue)
Written by Tae-Hyung "T" Kim, Ph.D.
  pcm2wav: Linux, Shell Scripting, Python을 써서 .pcm을 .wav로 파일 포맷 변환 (In Korean)
  https://aimldl.blog.me/221559323232
"""

import wave

# The parameters are prerequisite information. More specifically,
# channels, bit_depth, sampling_rate must be known to use this function.
class AudioSignalProcessing:
    def __init__( self ):
        pass
    
    # The parameters are prerequisite information. More specifically,
    # channels, bit_depth, sampling_rate must be known to use this function.
    def pcm2wav( self, pcm_file, wav_file, channels=1, bit_depth=16, sampling_rate=16000 ):
    
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
    #   https://tutel.me/c/programming/questions/46538867/at￣tributeerror+wave_write+instance+has+no+attribute+39__exit__39
    # But the code doens't look neat and more number of lines are required.