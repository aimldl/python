#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_pcm2wav
An example Python script that
  converts .pcm files in directory 'audio/pcm' to .wav files in directory 'audio/wav'.
  
audiosp module has class AudioSignalProcessing where pcm2wav is a member function.

This script is designed to run by run_pcm2wav
  $ ./run_pcm2wav
because it's assumed os.curdir is where run_pcm2wav is located.

@author: aimldl
"""  

import audiosp
import os
from playsound import playsound

if __name__ == '__main__':
    asp = audiosp.AudioSignalProcessing()

    # Get the list of .pcm file list in the current directory
    #files     = os.listdir( os.curdir )
    dir_pcm    = 'pcm'
    dir_wav    = 'wav'
    dir_input_files  = os.curdir + '/' + dir_pcm
    dir_output_files = os.curdir + '/' + dir_wav
    
    input_files     = os.listdir( dir_input_files )
    input_file_list = []
    #file_list = ['001.pcm','002.pcm','003.pcm']  # For debugging
    for input_file in input_files:
        # If file is a .pcm file, append it to the file list
        if '.pcm' in input_file:
            input_file_list.append( input_file )
    print( input_file_list )  # Debugging
    
    # Configuration for pcm2wav
    channels      = 1     # Mono channel
    bit_depth     = 16    # bit
    sampling_rate = 44100 # Hz

    # Finish the infinite loop when all file_list is completed.
    for file_pcm in input_file_list:
        file_wav = file_pcm.replace('.pcm','.wav')
        print('Converting ' + file_pcm + ' to ' + file_wav + '...')
        
        source_file = dir_input_files  + '/' + file_pcm
        target_file = dir_output_files + '/' + file_wav
        asp.pcm2wav( source_file, target_file, channels, bit_depth, sampling_rate )
        
        print('Playing ' + file_wav + ' for testing purposes ...')
        playsound( target_file )