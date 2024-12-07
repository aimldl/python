'''
webrt_vad.py

Prerequisite:
+ Install webrtcvad
  $ pip install webrtcvad
+ Install other packages such as numpy, matplotlib, and scipy
  $ pip install package_name
  
fs sampling rate

py-webrtcvad, https://github.com/wiseman/py-webrtcvad/
Voice activity detection example, https://www.kaggle.com/holzner/voice-activity-detection-example
[This example didn't run, so I had to fix some parts.]
'''

import os
import numpy as np
import matplotlib.pyplot as plt
import webrtcvad
import struct
import IPython.display as ipd

from scipy.io import wavfile

class WebRtVad:
    # This class is assumed to be a singleton.
    # Constructor
    def __init__( self ):
        self.vad = webrtcvad.Vad()
        self.vad.set_mode(3)
        self.configure()
        
    def configure( self ):
        self.window_duration = 0.03 # duration in seconds
        self.bytes_per_sample = 2

    def test_run( self ):
        # Read in the input .wav file
        #file = './english-0.wav'
        if __name__ == '__main__':
            file = './audio_files/english-0.wav'
        else:
            file = './vad/audio_files/english-0.wav'
        samples, fs = self.read_wav( file )
        num_samples = len(samples)  # 57920
        samples_per_window = int( self.window_duration * fs + 0.5 )
        
        # Verify the input file
        self.play_audio( samples, fs )
        self.plot( samples, title='Input Signal' )
        
        norm_samples, y_max = self.normalize( samples )
        self.play_audio( norm_samples, fs )
        self.plot( norm_samples, title='Normalized Input Signal' )
        
        # Apply VAD
        #   CAUTION:
        #   samples shouldn't be normalized because the format h is short int. 
        #   So pack expects a sequence of integers as the input.
        #   Otherwise,
        #   *** struct.error: required argument is not an integer
        raw_samples = struct.pack( "%dh" % len(samples), *samples)
        segments    = self.get_segments( raw_samples, num_samples, fs, samples_per_window )
        self.plot_segments( norm_samples, segments )

    def read_wav( self, file ):
        fs, samples = wavfile.read( file )

        return samples, fs

    def normalize( self, samples ):
        '''
        Peak normalization of the input audio signal
        i.e. normalize the input audio signal or data with the maximum value
        '''
        y_max        = max( abs(samples) )
        norm_samples = samples / y_max

        return norm_samples, y_max
    
    def play_audio( self, samples, fs ):
        ipd.Audio( samples, rate=fs )

    def plot( self, samples, title='Input File' ):
        plt.figure(figsize = (10,7))
        plt.plot( samples )
        plt.grid()
        plt.title( title )
        plt.xlabel( 'sample' )
        plt.ylabel( 'Amplitude' )

    def get_segments( self, raw_samples, num_samples, fs, samples_per_window ):
        '''
        segment_dict is a dictionary of {start, stop, is_speech} for a window.
        Each window's sample starts from start and ends at stop.
        Byte-wise, a window starts from from_ and ends at to.
        
        segments_dicts is a collection of all the windows.
        '''
        segments_dicts = []
        for start in np.arange(0, num_samples, samples_per_window):
            from_ = start * self.bytes_per_sample
            stop  = min( start + samples_per_window, num_samples )  # For the last frame
            to    = stop * self.bytes_per_sample
            this_window  = raw_samples[ from_:to ]

            # TODO: Fix an error from here
            #   ipdb> webrtcvad.Error: Error while processing frame
            is_speech    = self.vad.is_speech( this_window, sample_rate=fs )
            segment_dict = dict( start=start, stop=stop, is_speech=is_speech)
            segments_dicts.append( segment_dict )
        return segments_dicts

    def plot_segments( self, samples, segments ):
        
        self.plot( samples, 'Speech Samples' )
        
        peak_value = max( abs(samples) )
        
        # Overlay the speech segments over the input waveform
        for segment in segments:
            if segment['is_speech']:
                x = [ segment['start'], segment['stop'] - 1]
                y = [ peak_value, peak_value ]
                #y = [ 1, 1 ]
                # plot segment identifed as speech
                plt.plot(x, y, color = 'orange')
        plt.show()

    def run( self, input_, num_samples, format_='samples' ):
        if format_ == 'file':
            assert isinstance( input_, str ), 'When the format is file, input_ must be a string.'
            # Read in the input .wav file
            file = input_
            #file = './english-0.wav'
            #file = '../audio_files/english-0.wav'
            samples, fs = self.read_wav( file )
        elif format_ == 'samples':
            # assert isinstance( input_[0], numpy.ndarray ) numpy.ndarray
            assert isinstance( input_[1], int ), 'input_[1] must be sampling rate which is an integer.'
            samples   = input_[0]
            fs        = input_[1]
            data_type = samples.dtype.name
            if data_type == 'float64':
                samples = samples.astype(int)
            # Note samples must be integers ('int16'?)
        
        samples_per_window = int( self.window_duration * fs + 0.5 )

        # Verify the input file
#        if self.config.debug:
#            self.play_audio( samples, fs )
#            self.plot( samples, title='Input Signal' )
#            self.play_audio( norm_samples, fs )
#            self.plot( norm_samples, title='Normalized Input Signal' )
        
        # Apply VAD
        #   CAUTION:
        #   samples shouldn't be normalized because the format h is short int. 
        #   So pack expects a sequence of integers as the input.
        #   Otherwise,
        #   *** struct.error: required argument is not an integer
        
        raw_samples = struct.pack( "%dh" % num_samples, *samples)
        segments    = self.get_segments( raw_samples, num_samples, fs, samples_per_window )
        self.plot_segments( samples, segments )

if __name__ == '__main__':
    vad = WebRtVad()
    vad.test_run()