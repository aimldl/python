# -*- coding: utf-8 -*-
# test_python_speech_features.py

from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav

( rate, sig ) = wav.read( 'english.wav' )
mfcc_feat = mfcc( sig, rate )
d_mfcc_feat = delta( mfcc_feat, 2)
fbank_feat = logfbank( sig, rate )

#print( fbank_feat[1:3,:] )
print('mfcc_feat')
print( mfcc_feat[1:2,:] )

print('d_mfcc_feat')
print( d_mfcc_feat[1:2,:] )

print('fbank_feat')
print( fbank_feat[1:2,:] )